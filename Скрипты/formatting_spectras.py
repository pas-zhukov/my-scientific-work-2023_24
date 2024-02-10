import pandas as pd
from matplotlib import pyplot as plt

file_1 = "../Измерения/Со спектрометра Клинкова/09.02.24/091/transparent.csv"
file_2 = "../Измерения/Со спектрометра Клинкова/09.02.24/091/dark.csv"

file_result = "../Измерения/По образцам/091/091 Цикл №900+.xlsx"

measurements_1 = pd.read_csv(file_1, delimiter=";", decimal=",", names=["Wavelength, nm", "Transmittance, % (bleached)"])
measurements_2 = pd.read_csv(file_2, delimiter=";", decimal=",", names=["Wavelength, nm", "Transmittance, % (colored)"])

measurements = pd.merge(measurements_1, measurements_2, on=["Wavelength, nm"])

measurements.to_excel(file_result, index=False)

fig, ax = plt.subplots(1, 1, figsize=(10, 7))

ax.plot(measurements["Wavelength, nm"], measurements["Transmittance, % (bleached)"], 'b-')
ax.plot(measurements["Wavelength, nm"], measurements["Transmittance, % (colored)"], 'r-')

ax.set_ylabel("Пропускание, %")
ax.set_xlabel("Длина волны, нм")

ax.set_xlim(measurements['Wavelength, nm'][0], measurements['Wavelength, nm'].iloc[-1])

ax.grid()
fig.tight_layout()
fig.show()

