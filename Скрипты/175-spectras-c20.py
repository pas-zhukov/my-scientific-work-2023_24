import pandas as pd
import scipy.interpolate
from matplotlib import pyplot as plt
import numpy as np

# Устанавливаем шрифт Arial для всех текстовых элементов
plt.rcParams['font.family'] = 'Arial'
# plt.rcParams['font.size'] = 12  # Можно задать размер шрифта по умолчанию

def main():
    file_1 = "../Измерения/Со спектрометра Клинкова/24.05.24/175 обесцв.csv"
    file_2 = "../Измерения/Со спектрометра Клинкова/24.05.24/175 окраш.csv"

    mes = [file_1, file_2]
    dfs = []
    for m in mes:
        dfs.append(pd.read_csv(m, delimiter=";", decimal=",", names=["wl", "t"]))

    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    i = 0
    j = 0
    k = 0
    colors = ["deepskyblue", "b", "r", "maroon"]
    txt = ["Bleached", "Colored", 100, 100, 900, 900, 1000, 1000]
    for df in dfs:
        if i % 2 == 0:
            ax.plot(df["wl"], df["t"], color=colors[k], label=txt[j].__str__())
        else:
            ax.plot(df["wl"], df["t"], color=colors[k])
        i += 1
        j += 1
        if i == 1:
            i = 0
            k += 1

    ax.minorticks_on()

    ax.set_ylabel("Transmittance, %", size=24)
    ax.set_xlabel("Wavelength, nm", size=24)

    # Увеличиваем толщину осей (рамки графика)
    for spine in ax.spines.values():
        spine.set_linewidth(2)  # Толщина рамки графика

    # Увеличиваем толщину делений (тиков)
    ax.tick_params(axis="both", direction="in", length=8, labelsize=18, width=2)

    ax2 = ax.secondary_yaxis("right")
    ax2.tick_params(axis="both", direction="in", length=8, labelcolor="white", width=2)
    ax3 = ax.secondary_xaxis("top")
    ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white", width=2)

    # Настройка минорных делений
    ax.minorticks_on()
    ax.tick_params(which='minor', direction='in', length=4, width=1.5)  # Увеличиваем толщину минорных тиков
    ax.xaxis.set_minor_locator(plt.MultipleLocator(25))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(5))

    ax2.minorticks_on()
    ax2.tick_params(which='minor', direction='in', length=4, width=1.5)  # Увеличиваем толщину минорных тиков
    ax2.yaxis.set_minor_locator(plt.MultipleLocator(5))

    ax3.minorticks_on()
    ax3.tick_params(which='minor', direction='in', length=4, width=1.5)  # Увеличиваем толщину минорных тиков
    ax3.xaxis.set_minor_locator(plt.MultipleLocator(25))

    # Изменение положения легенды
    ax.legend(fontsize='20', loc='upper right', bbox_to_anchor=(0.95, 0.95))

    ax.set_ylim(50, 100)
    ax.set_xlim(350, 900)

    fig.tight_layout()
    plt.show()

    fig.savefig("../Картинки/Спектры/Спектры гладкого образца.png", dpi=500)


def smooth(a):
    w = np.hanning(1)
    b = np.convolve(w / w.sum(), a, mode='same')
    return b


if __name__ == "__main__":
    main()