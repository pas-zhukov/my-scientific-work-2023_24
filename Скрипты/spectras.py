import pandas as pd
from matplotlib import pyplot as plt

file = "../Измерения/Со спектрометра Клинкова/22.12.23/water_spectra_2.csv"

TITLE = "Спектр воды 2"

measurements = pd.read_csv(file, delimiter=";", decimal=",", names=["wavelength", "intensity"])


fig, ax = plt.subplots(1, 1, figsize=(10, 7))

ax.plot(measurements["wavelength"], measurements["intensity"], 'b-')

ax.set_title(TITLE)
ax.set_ylabel("Пропускание, %")
ax.set_xlabel("Длина волны, нм")

ax.set_xlim(measurements['wavelength'][0], measurements['wavelength'].iloc[-1])

ax.grid()
fig.tight_layout()
fig.show()

fig.savefig("../Картинки/Спектры/После 10 циклов сухие + погруженные в воду (22.12.23)/" + TITLE + ".png", dpi=300)