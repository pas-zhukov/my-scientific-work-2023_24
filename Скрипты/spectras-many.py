import pandas as pd
from matplotlib import pyplot as plt

file_1 = "../Измерения/Со спектрометра Клинкова/24.05.24/175 обесцв.csv"
file_2 = "../Измерения/Со спектрометра Клинкова/24.05.24/175 окраш.csv"

TITLE = "Образец 181 после осаждения (сухой + в воде)"

spectra_1 = pd.read_csv(file_1, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_2 = pd.read_csv(file_2, delimiter=";", decimal=",", names=["wavelength", "intensity"])


fig, ax = plt.subplots(1, 1, figsize=(10, 7))

ax.plot(spectra_1["wavelength"], spectra_1["intensity"], 'r-')
ax.plot(spectra_2["wavelength"], spectra_2["intensity"], 'b-')

# ax.legend(["Сухой образец", "Образец, погруженный в воду"])

ax.set_title(TITLE)
ax.set_ylabel("Пропускание, %")
ax.set_xlabel("Длина волны, нм")

ax.set_xlim(spectra_1['wavelength'][0], spectra_1['wavelength'].iloc[-1])

ax.grid()
fig.tight_layout()
fig.show()

# fig.savefig("../Картинки/Спектры/Сухие + погруженные в воду, после осаждения (19.01.23)/" + TITLE + ".png", dpi=300)