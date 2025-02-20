import pandas as pd
import scipy.interpolate
from matplotlib import pyplot as plt
import numpy as np


def main():
    file_1 = "../Измерения/Со спектрометра Клинкова/09.02.24/091/dark.csv"
    file_2 = "../Измерения/Со спектрометра Клинкова/09.02.24/091/transparent.csv"

    mes = [file_1, file_2]
    dfs = []
    for m in mes:
        dfs.append(pd.read_csv(m, delimiter=";", decimal=",", names=["wl", "t"]))




    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    i = 0
    j = 0
    k=0
    colors = ["deepskyblue", "m", "r", "maroon"]
    txt = ["20 (bleached)", "20 (colored)", 100, 100, 900, 900, 1000, 1000]
    for df in dfs:
        if i % 2 == 0:
            ax.plot(df["wl"], df["t"], color=colors[k], label="Сycle №"+txt[j].__str__())
        else:
            ax.plot(df["wl"], df["t"], color=colors[k])
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

    # ax.legend(fontsize='14')

    ax.set_ylim(50, 100)
    ax.set_xlim(350, 900)

    fig.tight_layout()
    fig.show()

    fig.savefig("../091 спектры", dpi=500)


def smooth(a):
    w = np.hanning(1)
    b = np.convolve(w / w.sum(), a, mode='same')
    return b


if __name__ == "__main__":
    main()
