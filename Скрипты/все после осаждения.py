import pandas as pd
from matplotlib import pyplot as plt

file_1 = "../Измерения/Со спектрометра Клинкова/15.12.23/nio/sample_091.csv"
file_2 = "../Измерения/Со спектрометра Клинкова/15.12.23/nio/sample_094.csv"
file_3 = "../Измерения/Со спектрометра Клинкова/15.12.23/nio/sample_099.csv"
file_4 = "../Измерения/Со спектрометра Клинкова/15.12.23/nio/sample_103.csv"
file_5 = "../Измерения/Со спектрометра Клинкова/15.12.23/nio/sample_175.csv"
file_6 = "../Измерения/Со спектрометра Клинкова/15.12.23/nio/sample_181.csv"


TITLE = "Сравнительный спектр образцов на 103 цикле"


spectra_1 = pd.read_csv(file_1, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_2 = pd.read_csv(file_2, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_3 = pd.read_csv(file_3, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_4 = pd.read_csv(file_4, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_5 = pd.read_csv(file_5, delimiter=";", decimal=",", names=["wavelength", "intensity"])
spectra_6 = pd.read_csv(file_6, delimiter=";", decimal=",", names=["wavelength", "intensity"])



fig, ax = plt.subplots(1, 1, figsize=(10, 7))

ax.plot(spectra_1["wavelength"], spectra_1["intensity"], 'r-')
ax.plot(spectra_2["wavelength"], spectra_2["intensity"], 'y-')
ax.plot(spectra_3["wavelength"], spectra_3["intensity"], 'g-')
ax.plot(spectra_4["wavelength"], spectra_4["intensity"], 'b-')
ax.plot(spectra_5["wavelength"], spectra_5["intensity"], 'r--')
ax.plot(spectra_6["wavelength"], spectra_6["intensity"], 'y--')


ax.legend(["Образец 091 - в окрашенном состоянии",
           "Образец 094 - в окрашенном состоянии",
           "Образец 099 - в окрашенном состоянии",
           "Образец 103 - в окрашенном состоянии",
           "Образец 091 - в обесцвеченном состоянии",
           "Образец 094 - в обесцвеченном состоянии",
           "Образец 099 - в обесцвеченном состоянии",
           "Образец 103 - в обесцвеченном состоянии",
           ])


ax.set_title(TITLE)
ax.set_ylabel("Пропускание, %")
ax.set_xlabel("Длина волны, нм")

ax.set_xlim(spectra_1['wavelength'][0], spectra_1['wavelength'].iloc[-1])

ax.grid()
fig.tight_layout()
fig.show()

fig.savefig("../Картинки/Спектры/В окрашенном и обесцвеченном состоянии после 100 цикла (26.12.23)/" + TITLE + ".png", dpi=300)