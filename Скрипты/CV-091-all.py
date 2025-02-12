import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

plt.rcParams['font.family'] = 'Arial'

cor_file1_10 = "../Измерения/20.12.23/097_cv.cor"
cor_file100 = "../Измерения/26.12.23/091_cv_26.12.cor"
cor_file1000 = "../Измерения/28.02.24/091_CV_2cycles_10mVs_28.02.cor"
cor_file1800 = "../Измерения/27.06.24/091_CV_10mVs_27.06.cor"

sample = PotentiostatMeasurements(cor_file1_10)
sample100 = PotentiostatMeasurements(cor_file100)
sample1000 = PotentiostatMeasurements(cor_file1000)
sample1800 = PotentiostatMeasurements(cor_file1800)

fig, ax = plt.subplots(1, 1, figsize=(10, 8))

per_cycle = 1800
s1 = per_cycle * 1
s2 = per_cycle * 11
current = list(map(lambda x: 1000 * x / 5, sample.current))
line1, = ax.plot(sample.voltage[-1800:-1], list(map(lambda x: 1000 * x / 5, sample.current))[-1800:-1], color='aqua', label="10'th cycle")
line2, = ax.plot(sample100.voltage[-1800:-1], list(map(lambda x: 1000 * x / 5, sample100.current))[-1800:-1], color='deepskyblue', label="100'th cycle")
line3, = ax.plot(sample1000.voltage[-1800:-1], list(map(lambda x: 1000 * x / 5, sample1000.current))[-1800:-1], color='teal', label="1000'th cycle")
line4, = ax.plot(sample1800.voltage[-1800:-1], list(map(lambda x: 1000 * x / 5, sample1800.current))[-1800:-1], color='midnightblue', label="1800'th cycle")

# arrow = ax.arrow(0.39, 0.05, 0.04, 0.05, width=0.002, color="salmon")
# plt.annotate("cycle increase", (0.37, 0.05), (0.25, 0.05), color="tomato", fontsize=20)

ax.set_aspect(2)
#ax.set_title("Sample 091")

ax.set_xlabel(r"Sample potential, V", size=20)
ax.set_ylabel(r"Current density, mA/cm²", size=20)

# Увеличение толщины осей
for spine in ax.spines.values():
    spine.set_linewidth(2)

# Увеличение толщины тиков
ax.tick_params(axis="both", direction="in", length=8, labelsize=18, width=2)

# Добавление легенды с небольшим смещением от верхнего левого угла
legend = ax.legend(fontsize='20', loc='upper left', bbox_to_anchor=(0.02, 0.98))
plt.setp(legend.get_title(), fontsize='20', color='black')
legend.set_title("NW250")


ax2 = ax.secondary_yaxis("right")
ax2.tick_params(axis="both", direction="in", length=8, labelcolor="white", width=2)
ax3 = ax.secondary_xaxis("top")
ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white", width=2)

ax.minorticks_on()
ax.tick_params(which='minor', direction='in', length=4, width=1.5)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.025))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.01))
ax2.minorticks_on()
ax2.tick_params(which='minor', direction='in', width=1.5)
ax2.yaxis.set_minor_locator(plt.MultipleLocator(0.01))
ax3.minorticks_on()
ax3.tick_params(which='minor', direction='in', width=1.5)
ax3.xaxis.set_minor_locator(plt.MultipleLocator(0.025))

ax.set_xlim(-0.21, 0.7)
ax.set_ylim(-0.17, 0.26)

# ax.grid()
fig.tight_layout()
plt.show()

fig.savefig("../Картинки/ЦВА/Sample091 10 100 1000 1800.png", dpi=500)