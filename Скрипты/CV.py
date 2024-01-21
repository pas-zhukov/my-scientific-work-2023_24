import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/20.12.23/097_cv.cor"

sample_091 = PotentiostatMeasurements(cor_file)
sample_094 = PotentiostatMeasurements("../Измерения/20.12.23/094_cv.cor")
sample_099 = PotentiostatMeasurements("../Измерения/20.12.23/099_cv.cor")
sample_103 = PotentiostatMeasurements("../Измерения/20.12.23/103_cv.cor")

fig, ax = plt.subplots(1, 1, figsize=(10, 10))

# :2000
# -2000:-1
# cycle = -2000:-1
ax.set_title("Сравнительный график ЦВА образцов на 10 цикле")

ax.plot(sample_091.voltage[-1805:-1], sample_091.current[-1805:-1], 'r-')
ax.plot(sample_094.voltage[-1805:-1], sample_094.current[-1805:-1], 'g-')
ax.plot(sample_099.voltage[-1805:-1], sample_099.current[-1805:-1], 'b-')
ax.plot(sample_103.voltage[-1805:-1], sample_103.current[-1805:-1], 'y-')

ax.set_xlabel("Потенциал образца, В")
ax.set_ylabel("Плотность тока, А")

ax.legend(["Образец 091", "Образец 094", "Образец 099", "Образец 103"])

# ax.set_yticks([.001 * i for i in range(-2, 8, 1)])
ax.set_xticks([.1 * i for i in range(-2, 8, 1)])

ax.grid()
fig.tight_layout()
fig.show()

# fig.savefig("../Картинки/ЦВА/20.12.23/Сравнительный график ЦВА образцов на 10 цикле.png", dpi=300)
