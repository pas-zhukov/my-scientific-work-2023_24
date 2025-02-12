import pandas as pd
import scipy.interpolate
from matplotlib import pyplot as plt
import numpy as np


def main():
    plt.rcParams['font.family'] = 'Arial'

    c15d = "../Измерения/Со спектрометра Клинкова/22.12.23/cycles/91/15_dark.csv"
    c15l = "../Измерения/Со спектрометра Клинкова/22.12.23/cycles/91/15_light.csv"
    c103d = "../Измерения/Со спектрометра Клинкова/26.12.23/091_dark_3.csv"
    c103l = "../Измерения/Со спектрометра Клинкова/26.12.23/091_light_3.csv"
    # c900d = "../Измерения/Со спектрометра Клинкова/09.02.24/091/dark.csv"
    # c900l = "../Измерения/Со спектрометра Клинкова/09.02.24/091/transparent.csv"
    c1000l = "../Измерения/Со спектрометра Клинкова/28.02.24/091/ц1000 обесцв сост.csv"
    c1000d = "../Измерения/Со спектрометра Клинкова/28.02.24/091/ц1000 окр сост.csv"
    c1800l = "../Измерения/Со спектрометра Клинкова/24.05.24/091 ц1811 обесцв.csv"
    c1800d = "../Измерения/Со спектрометра Клинкова/24.05.24/091 ц1811 окр.csv"

    mes = [c15l, c15d, c103l, c103d, c1000l, c1000d, c1800l, c1800d]
    dfs = []
    for m in mes:
        dfs.append(pd.read_csv(m, delimiter=";", decimal=",", names=["wl", "t"]))

    dfs[2].t += 0
    dfs[3].t += 0
    dfs[4].t += -1.3
    dfs[5].t += -1.3
    dfs[6].t += 1.2
    dfs[7].t += 1.2

    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    i = 0
    j = 0
    k = 0
    colors = ["aqua", "deepskyblue", "teal", "midnightblue", 'green']
    txt = [15, 15, 100, 100, 1000, 1000, 1800, 1800]
    for df in dfs:
        if i % 2 == 0:
            ax.plot(df["wl"], df["t"], color=colors[k], label="NW250 cycle " + txt[j].__str__(), linewidth=2)
        else:
            ax.plot(df["wl"], df["t"], color=colors[k], linewidth=2)
        i += 1
        j += 1
        if i == 2:
            i = 0
            k += 1

    ax.minorticks_on()

    ax.set_ylabel("Transmittance, %", size=24)
    ax.set_xlabel("Wavelength, nm", size=24)

    # Увеличение толщины осей
    for spine in ax.spines.values():
        spine.set_linewidth(2)

    # Увеличение толщины тиков
    ax.tick_params(axis="both", direction="in", length=8, labelsize=18, width=2)

    ax2 = ax.secondary_yaxis("right")
    ax2.tick_params(axis="both", direction="in", length=8, labelcolor="white", width=2)
    ax3 = ax.secondary_xaxis("top")
    ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white", width=2)

    ax.minorticks_on()
    ax.tick_params(which='minor', direction='in', length=4, width=1.5)
    ax.xaxis.set_minor_locator(plt.MultipleLocator(25))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(5))
    ax2.minorticks_on()
    ax2.tick_params(which='minor', direction='in', width=1.5)
    ax2.yaxis.set_minor_locator(plt.MultipleLocator(5))
    ax3.minorticks_on()
    ax3.tick_params(which='minor', direction='in', width=1.5)
    ax3.xaxis.set_minor_locator(plt.MultipleLocator(25))

    # Добавление легенды в правый нижний угол с отступом от края
    ax.legend(fontsize='20', loc='lower right', bbox_to_anchor=(0.95, 0.05))

    ax.set_ylim(50, 100)
    ax.set_xlim(350, 900)

    fig.tight_layout()
    plt.show()

    fig.savefig("../Картинки/Спектры/Спектры 91 образца.png", dpi=500)


def smooth(a):
    w = np.hanning(1)
    b = np.convolve(w / w.sum(), a, mode='same')
    return b


if __name__ == "__main__":
    main()