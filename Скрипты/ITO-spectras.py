import pandas as pd
import scipy.interpolate
from matplotlib import pyplot as plt
import numpy as np


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
    # reflectance = measurements["refl"]
    # w = np.hanning(5)
    # reflectance = np.convolve(w / w.sum(), reflectance, mode='same')

    # ax.plot(measurements["wavelength"], reflectance, 'b-')

    # ax.set_aspect(2000)
    # ax2.set_aspect(2000)



    ax.set_ylabel("Transmittance, %", size=24)
    ax.set_xlabel("Wavelength, nm", size=24)
    ax2.set_ylabel("Reflectance, %", size=24)

    ax.tick_params(axis="both", direction="in", length=8, labelsize=20)
    ax2.tick_params(axis="both", direction="in", length=8, labelsize=20)
    ax3 = ax.secondary_xaxis("top")
    ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white")

    ax.tick_params(axis="both", direction="in", length=8, labelsize=18)

    ax3 = ax.secondary_xaxis("top")
    ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white")

    ax.minorticks_on()
    ax.tick_params(which='minor', direction='in', length=2)
    ax.xaxis.set_minor_locator(plt.MultipleLocator(20))
    ax2.xaxis.set_minor_locator(plt.MultipleLocator(20))
    ax.yaxis.set_minor_locator(plt.MultipleLocator(5))
    ax2.minorticks_on()
    ax2.tick_params(which='minor', direction='in')
    ax2.yaxis.set_minor_locator(plt.MultipleLocator(5))
    ax3.minorticks_on()
    ax3.tick_params(which='minor', direction='in')
    ax3.xaxis.set_minor_locator(plt.MultipleLocator(20))

    arrow = ax.arrow(800, 15, 100, 0, width=0.5, color="grey")
    arrow2 = ax.arrow(600, 80, -100, 0, width=0.5, color="grey")


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
