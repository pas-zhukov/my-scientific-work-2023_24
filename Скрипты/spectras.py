import pandas as pd
from matplotlib import pyplot as plt
import pathlib

file = "../Измерения/Со спектрометра Клинкова/15.12.23/nio/sample_181.csv"

TITLE = "181 После осаждения - сухой"

path_result = "../Измерения/По образцам/181/"

if not pathlib.Path(path_result).exists():
    pathlib.Path(path_result).mkdir()

measurements = pd.read_csv(file, delimiter=";", decimal=",", names=["Wavelength, nm", "Transmittance, %"])

measurements.to_excel(path_result + TITLE + ".xlsx", index=False)

fig, ax = plt.subplots(1, 1, figsize=(10, 7))

ax.plot(measurements["Wavelength, nm"], measurements["Transmittance, %"], 'b-')

ax.set_title(TITLE)
ax.set_ylabel("Пропускание, %")
ax.set_xlabel("Длина волны, нм")

# ax.set_xlim(measurements["Wavelength, nm"][0], measurements["Transmittance, %"].iloc[-1])

ax.grid()
fig.tight_layout()
fig.show()

# fig.savefig("../Картинки/Спектры/После 10 циклов сухие + погруженные в воду (22.12.23)/" + TITLE + ".png", dpi=300)
