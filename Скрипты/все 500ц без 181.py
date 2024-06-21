import pandas as pd
import scipy.interpolate
from matplotlib import pyplot as plt
import numpy as np


def main():
    c15d = "../Измерения/Со спектрометра Клинкова/09.02.24/091/dark.csv"
    c15l = "../Измерения/Со спектрометра Клинкова/09.02.24/091/transparent.csv"
    c103d = "../Измерения/Со спектрометра Клинкова/24.05.24/094 ц500 окраш.csv"
    c103l = "../Измерения/Со спектрометра Клинкова/24.05.24/094 ц500 обесцв.csv"
    c900d = "../Измерения/Со спектрометра Клинкова/09.02.24/099/dark.csv"
    c900l = "../Измерения/Со спектрометра Клинкова/09.02.24/099/transparent.csv"
    c1000d = "../Измерения/Со спектрометра Клинкова/27.03.24/103/ц500 окр.csv"
    c1000l = "../Измерения/Со спектрометра Клинкова/27.03.24/103/ц500 обесцв.csv"



    mes = [c15l, c15d, c103l, c103d, c900l, c900d, c1000l, c1000d]
    dfs = []
    for m in mes:
        dfs.append(pd.read_csv(m, delimiter=";", decimal=",", names=["wl", "t"]))


    # dfs[2].t += 0
    # dfs[3].t += 0
    # dfs[4].t += -0.8
    # dfs[5].t += -0.8
    # dfs[6].t += -1.2
    # dfs[7].t += -1.2
    # dfs[8].t += +0.7
    # dfs[9].t += 0.7



    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    i = 0
    j = 0
    k=0
    colors = ["deepskyblue", "m", "r", "maroon",  'orange']
    txt = ["250","250", "400","400", "700","700", "1150", "1150",  "181","181", ]
    for df in dfs:
        if i % 2 == 0:
            pass
            # ax.plot(df["wl"], df["t"], color=colors[k])
        else:
            ax.plot(df["wl"], df["t"], color=colors[k], label="Пористый ITO - "+txt[j].__str__()+" нм; NiO - 20 нм")
        i+=1
        j+=1
        if i == 2:
            i = 0
            k += 1

    ax.minorticks_on()

    ax.set_ylabel("Пропускание, %", size=20)
    ax.set_xlabel("Длина волны, нм", size=20)

    ax.tick_params(axis="both", direction="in", length=8, labelsize=16)

    ax2 = ax.secondary_yaxis("right")
    ax2.tick_params(axis="both", direction="in", length=8, labelcolor="white")
    ax3 = ax.secondary_xaxis("top")
    ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white")

    ax.minorticks_on()
    ax.tick_params(which='minor', direction='in', length=2)
    ax.xaxis.set_minor_locator(plt.MultipleLocator(25))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
    ax2.minorticks_on()
    ax2.tick_params(which='minor', direction='in')
    ax2.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
    ax3.minorticks_on()
    ax3.tick_params(which='minor', direction='in')
    ax3.xaxis.set_minor_locator(plt.MultipleLocator(25))

    ax.legend(fontsize='14')

    ax.set_ylim(0, 100)
    ax.set_xlim(350, 900)

    fig.tight_layout()
    plt.show()

    fig.savefig("../Картинки/Спектры/все образцы 500ц без 181", dpi=500)


def smooth(a):
    w = np.hanning(1)
    b = np.convolve(w / w.sum(), a, mode='same')
    return b


if __name__ == "__main__":
    main()
