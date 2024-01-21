import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/20.12.23/097_cv.cor"

sample = PotentiostatMeasurements(cor_file)

fig, ax = plt.subplots(1, 1, figsize=(10, 10))

per_cycle = 1800
s1 = per_cycle * 1
s2 = per_cycle * 11
ax.plot(sample.voltage[0:1800], sample.current[0:1800], 'r-')
ax.plot(sample.voltage[s1:s2], sample.current[s1:s2], 'b-')



ax.set_title("Образец 091")

ax.set_xlabel("Потенциал образца, В")
ax.set_ylabel("Плотность тока, А")

ax.legend(["1 цикл", "2-10 циклы"])

# ax.set_yticks([.0001 * i for i in range(-15, 30, 5)])
ax.set_xticks([.1 * i for i in range(-2, 8, 1)])

ax.grid()
fig.tight_layout()
fig.show()

fig.savefig("../Картинки/ЦВА/20.12.23/091 первые 10 циклов.png", dpi=300)
