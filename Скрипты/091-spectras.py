import pandas as pd
import scipy.interpolate
from matplotlib import pyplot as plt
import numpy as np


def main():
    c15d = "../Измерения/Со спектрометра Клинкова/22.12.23/cycles/91/15_dark.csv"
    c15l = "../Измерения/Со спектрометра Клинкова/22.12.23/cycles/91/15_light.csv"
    c103d = "../Измерения/Со спектрометра Клинкова/26.12.23/091_dark_3.csv"
    c103l = "../Измерения/Со спектрометра Клинкова/26.12.23/091_light_3.csv"
    c900d = "../Измерения/Со спектрометра Клинкова/09.02.24/091/dark.csv"
    c900l = "../Измерения/Со спектрометра Клинкова/09.02.24/091/transparent.csv"
    c1000l = "../Измерения/Со спектрометра Клинкова/28.02.24/091/ц1000 обесцв сост.csv"
    c1000d = "../Измерения/Со спектрометра Клинкова/28.02.24/091/ц1000 окр сост.csv"

    mes = [c15l, c15d, c103l, c103d, c900l, c900d, c1000l, c1000d]
    dfs = []
    for m in mes:
        dfs.append(pd.read_csv(m, delimiter=";", decimal=",", names=["wl", "t"]))

    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    i = 0
    k=0
    colors = ["salmon", "coral", "red", "maroon"]
    for df in dfs:
        ax.plot(df["wl"], df["t"], color=colors[k])
        i+=1
        if i == 2:
            i = 0
            k += 1


    ax.set_ylabel("Пропускание, %", size=20)
    ax.set_xlabel("Длина волны, нм", size=20)

    ax.tick_params(axis="both", direction="in", length=8)

    ax.legend(["15", "15", "100", "100", "900", "900", "1000", "1000"])

    ax.set_ylim(0, 100)
    ax.set_xlim(350, 900)

    fig.tight_layout()
    fig.show()

    fig.savefig("../Картинки/Спектры/091 циклы", dpi=500)


def smooth(a):
    w = np.hanning(1)
    b = np.convolve(w / w.sum(), a, mode='same')
    return b


if __name__ == "__main__":
    main()
