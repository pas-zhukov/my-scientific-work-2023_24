import pandas as pd
import scipy.interpolate
from matplotlib import pyplot as plt
import numpy as np

plt.rcParams['font.family'] = 'Arial'

def main():
    ito700_r = "../Измерения/ito/rf_ITO700_eB_093.oli"
    ito700_t = "../Измерения/ito/tr_ITO700eB.oli"

    ito2000_r = "../Измерения/ito/r_s031_SITO_e-b_2000A.oli"
    ito2000_t = "../Измерения/ito/t_s031_SITO_e-b_2000A.oli"

    ito700_r_data = pd.read_csv(ito700_r, delimiter="\t", names=["wavelength", "refl"], skiprows=38, nrows=720)
    ito700_t_data = pd.read_csv(ito700_t, delimiter="\t", names=["wavelength", "transm"], skiprows=38, nrows=720)

    ito2000_r_data = pd.read_csv(ito2000_r, delimiter="\t", names=["wavelength", "refl"], skiprows=38, nrows=720)
    ito2000_t_data = pd.read_csv(ito2000_t, delimiter="\t", names=["wavelength", "transm"], skiprows=38, nrows=720)

    fig, ax = plt.subplots(1, 1, figsize=(10, 7))
    ax2 = ax.twinx()

    ax.plot(ito2000_t_data["wavelength"], smooth(ito2000_t_data["transm"]*100), "r")
    ax2.plot(ito2000_r_data["wavelength"], smooth(ito2000_r_data["refl"]*100), "r")

    ax.plot(ito700_t_data["wavelength"], smooth(ito700_t_data["transm"]*100), color="b")
    ax2.plot(ito700_r_data["wavelength"], smooth(ito700_r_data["refl"]*100), color="b")

    ax.legend(["NW700", "NW250"], loc="center", fontsize=20)

    ax.set_ylabel("Transmittance, %", size=24)
    ax.set_xlabel("Wavelength, nm", size=24)
    ax2.set_ylabel("Reflectance, %", size=24)

    # Увеличение толщины осей
    for axis in ['top', 'bottom', 'left', 'right']:
        ax.spines[axis].set_linewidth(2)
        ax2.spines[axis].set_linewidth(2)

    # Увеличение толщины тиков
    ax.tick_params(axis="both", direction="in", length=8, labelsize=20, width=2)
    ax2.tick_params(axis="both", direction="in", length=8, labelsize=20, width=2)

    ax3 = ax.secondary_xaxis("top")
    ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white", width=2)

    ax.minorticks_on()
    ax.tick_params(which='minor', direction='in', length=4, width=1.5)
    ax.xaxis.set_minor_locator(plt.MultipleLocator(20))
    ax2.xaxis.set_minor_locator(plt.MultipleLocator(20))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(5))
    ax2.minorticks_on()
    ax2.tick_params(which='minor', direction='in', width=1.5)
    ax2.yaxis.set_minor_locator(plt.MultipleLocator(5))
    ax3.minorticks_on()
    ax3.tick_params(which='minor', direction='in', width=1.5)
    ax3.xaxis.set_minor_locator(plt.MultipleLocator(20))

    arrow = ax.arrow(800, 19, 100, 0, width=0.3, head_width=1, head_length=10, color="grey")
    arrow2 = ax.arrow(690, 80, -100, 0, width=0.3, head_width=1, head_length=10, color="grey")

    arrow3 = ax.arrow(800, 19, -30, -6, width=0.4, head_width=0, head_length=0, color="grey")
    arrow4 = ax.arrow(690, 80, 30, 7, width=0.4, head_width=0, head_length=0, color="grey")

    ax.set_ylim(0, 100)
    ax2.set_ylim(0.00, 100)
    ax.set_xlim(380, 1030)

    fig.tight_layout()
    plt.show()

    fig.savefig("../Картинки/Спектры/Спектры ITO.png", dpi=500)


def smooth(a):
    w = np.hanning(1)
    b = np.convolve(w / w.sum(), a, mode='same')
    return b


if __name__ == "__main__":
    main()