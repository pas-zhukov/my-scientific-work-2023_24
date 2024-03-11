import pandas as pd
from matplotlib import pyplot as plt

file_1 = "../Измерения/Со спектрометра Клинкова/28.02.24/099/ц1000 окр сост.csv"
file_2 = "../Измерения/Со спектрометра Клинкова/28.02.24/099/ц1000 обесцв сост.csv"
file_3 = "../Измерения/Со спектрометра Клинкова/01.03.24/099/ц1047 окр сост.csv"
file_4 = "../Измерения/Со спектрометра Клинкова/01.03.24/099/ц1047 обесцв сост.csv"


TITLE = "Сравнительный спектр в 99 образца на 1000 и 1047 цикле"


spectra_1 = pd.read_csv(file_1, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_2 = pd.read_csv(file_2, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_3 = pd.read_csv(file_3, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_4 = pd.read_csv(file_4, delimiter=";", decimal=",", names=["wavelength", "intensity"])


fig, ax = plt.subplots(1, 1, figsize=(10, 7))

ax.plot(spectra_1["wavelength"], spectra_1["intensity"], 'r--')
ax.plot(spectra_2["wavelength"], spectra_2["intensity"], 'r-')
ax.plot(spectra_3["wavelength"], spectra_3["intensity"], 'b--')
ax.plot(spectra_4["wavelength"], spectra_4["intensity"], 'b-')

ax.legend(["Ц1000 окр. сост.",
           "Ц1000 обесцв. сост.",
           "Ц1047 окр. сост.",
           "Ц1047 обесцв. сост.",
           ])


ax.set_title(TITLE)
ax.set_ylabel("Пропускание, %")
ax.set_xlabel("Длина волны, нм")

ax.set_xlim(spectra_1['wavelength'][0], spectra_1['wavelength'].iloc[-1])

ax.grid()
fig.tight_layout()
fig.show()

fig.savefig("../Картинки/Спектры/" + TITLE + ".png", dpi=300)