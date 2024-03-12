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

    ax.plot(ito2000_t_data["wavelength"], smooth(ito2000_t_data["transm"]), "m-")
    ax2.plot(ito2000_r_data["wavelength"], smooth(ito2000_r_data["refl"]), "m-")

    ax.plot(ito700_t_data["wavelength"], smooth(ito700_t_data["transm"]), color="pink")
    ax2.plot(ito700_r_data["wavelength"], smooth(ito700_r_data["refl"]), color="pink")
    # reflectance = measurements["refl"]
    # w = np.hanning(5)
    # reflectance = np.convolve(w / w.sum(), reflectance, mode='same')

    # ax.plot(measurements["wavelength"], reflectance, 'b-')

    # ax.set_aspect(2000)
    # ax2.set_aspect(2000)

    ax.set_ylabel("Transmittance", size=20)
    ax.set_xlabel("Wavelength", size=20)
    ax2.set_ylabel("Reflectance", size=20)

    ax.tick_params(axis="both", direction="in", length=8)
    ax2.tick_params(axis="both", direction="in", length=8)

    ax.set_ylim(0, 1)
    ax2.set_ylim(0.00, 1)
    ax.set_xlim(380, 1100)

    fig.tight_layout()
    fig.show()

    # fig.savefig("../Картинки/Спектры/П.png", dpi=300)


def smooth(a):
    w = np.hanning(1)
    b = np.convolve(w / w.sum(), a, mode='same')
    return b


if __name__ == "__main__":
    main()
