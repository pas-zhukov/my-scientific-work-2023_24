import pandas as pd
from matplotlib import pyplot as plt

file_1 = "../Измерения/Со спектрометра Клинкова/26.12.23/103_light_3.csv"
file_2 = "../Измерения/Со спектрометра Клинкова/26.12.23/103_dark_3.csv"

file_result = "../Измерения/По образцам/103/103 Цикл №103.xlsx"

measurements_1 = pd.read_csv(file_1, delimiter=";", decimal=",", names=["Wavelength, nm", "Transmittance, % (bleached)"])
measurements_2 = pd.read_csv(file_2, delimiter=";", decimal=",", names=["Wavelength, nm", "Transmittance, % (colored)"])

measurements = pd.merge(measurements_1, measurements_2, on=["Wavelength, nm"])

measurements.to_excel(file_result, index=False)

fig, ax = plt.subplots(1, 1, figsize=(10, 7))

ax.plot(measurements["Wavelength, nm"][:800], measurements["Transmittance, % (bleached)"][:800], 'b-')
ax.plot(measurements["Wavelength, nm"][:800], measurements["Transmittance, % (colored)"][:800], 'r-')

ax.set_ylabel("Пропускание, %")
ax.set_xlabel("Длина волны, нм")

ax.set_xlim(measurements['Wavelength, nm'][0], measurements['Wavelength, nm'].iloc[-1])

ax.grid()
fig.tight_layout()
fig.show()

