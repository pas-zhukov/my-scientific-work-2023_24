import pandas as pd
import matplotlib.pyplot as plt


def process(file: str):
    buf = ""
    lines = []
    with open(file) as f:
        lines = f.readlines()
    for i in range(len(lines)):
        if len(lines[i]) < 19:
            continue
        if len(lines[i]) > 41:
            continue
        else:
            lines[i] = lines[i][:19] + " " + lines[i][19 + 1:]
            # buf += newline
    with open(file, "w") as f:
        f.writelines(lines)

    # print(buf)
    df = pd.read_csv(file, comment="/", encoding="cp1251", names=["time", "signal"], sep="\s+", decimal=".", skiprows=10)
    # print(df)
    df = df.round(2)
    per = df["signal"].get(0)
    df.signal /= per /100
    # print(df)

    fig, ax = plt.subplots(1, 1, figsize=(10, 7))

    ax.plot(df["time"], df["signal"])

    ax.minorticks_on()

    ax.set_ylabel("Пропускание, %", size=20)
    ax.set_xlabel("Время, с", size=20)

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

    ax.set_ylim(0, 100)
    # ax.set_xlim(0, 450)

    fig.tight_layout()

    fig.savefig(file + ".png", dpi=500)

    plt.close()


if __name__ == "__main__":
    file = "../Измерения/с комплекса/со спектрометра/04 12.04.24/094/142-147 классика + (-0.2)-1.0.mdrk"
    process(file)