import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/26.12.23/091_cv_26.12.cor"

sample_091 = PotentiostatMeasurements(cor_file)
# sample_094 = PotentiostatMeasurements("../Измерения/26.12.23/094_cv_26.12.cor")
# sample_099 = PotentiostatMeasurements("../Измерения/26.12.23/099_cv1_26.12.cor")
# sample_103 = PotentiostatMeasurements("../Измерения/26.12.23/103_cv_26.12.cor")

fig, ax = plt.subplots(1, 1, figsize=(10, 10))

ax.plot(sample_091.voltage[:2000], sample_091.current[:2000], 'r-')
# ax.plot(sample_094.voltage[:2000], sample_094.current[:2000], 'g-')
# ax.plot(sample_099.voltage[:2000], sample_099.current[:2000], 'b-')
# ax.plot(sample_103.voltage[:2000], sample_103.current[:2000], 'y-')

ax.set_xlabel("Потенциал образца, В")
ax.set_ylabel("Плотность тока, А")

ax.legend(["Образец 091", "Образец 094", "Образец 099", "Образец 103"])

ax.set_yticks([.001 * i for i in range(-2, 8, 1)])
ax.set_xticks([.1 * i for i in range(-2, 8, 1)])

ax.grid()
fig.tight_layout()
fig.show()

# fig.savefig("../Картинки/ЦВА/26.12.23/Сравнение ЦВА всех образцов (1 цикл)")
