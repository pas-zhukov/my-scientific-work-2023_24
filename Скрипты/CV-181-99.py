import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/06.02.24/181_CV_06.02.cor"
cor_file_2 = "../Измерения/20.12.23/099_cv.cor"

sample = PotentiostatMeasurements(cor_file)
sample2 = PotentiostatMeasurements(cor_file_2)

fig, ax = plt.subplots(1, 1, figsize=(10, 7))

per_cycle = 1800
s1 = per_cycle * 1
s2 = per_cycle * 11
current = list(map(lambda x: 1000 * x / 5, sample.current))
current2 = list(map(lambda x: 1000 * x /  5, sample2.current))
# ax.plot(sample.voltage[:s1], current[:s1], 'c-')
ax.plot(sample.voltage[-per_cycle:], current[-per_cycle:], 'deepskyblue')
ax.plot(sample2.voltage[-per_cycle:], current2[-per_cycle:], 'r')

# arrow = ax.arrow(0.39, 0.05, 0.04, 0.05, width=0.002)
# plt.annotate("рост № цикла", (0.37, 0.05), (0.25, 0.05))

# ax.set_aspect(1)
#ax.set_title("Sample 091")
ax.legend(["Пористый ITO - 700 нм; NiO - 20 нм;\n Добавлен проводящий подслой", "Пористый ITO - 700 нм; NiO - 20 нм"], fontsize=16)

ax.set_xlabel(r"Потенциал образца, $В$", size=28)
ax.set_ylabel(r"Плотность тока, $мА/см^2$", size=28)
ax.minorticks_on()

ax.tick_params(axis="both", direction="in", length=8, labelsize=22)

ax2 = ax.secondary_yaxis("right")
ax2.tick_params(axis="both", direction="in", length=8, labelcolor="white")
ax3 = ax.secondary_xaxis("top")
ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white")

ax.minorticks_on()
ax.tick_params(which='minor', direction='in', length=2)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax2.minorticks_on()
ax2.tick_params(which='minor', direction='in')
ax2.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax3.minorticks_on()
ax3.tick_params(which='minor', direction='in')
ax3.xaxis.set_minor_locator(plt.MultipleLocator(0.05))


ax.set_xlim(-0.21, 0.7)
ax.set_ylim(-0.91, 1.2)

# ax.grid()
fig.tight_layout()
plt.show()

fig.savefig("../ЦВА 181+99", dpi=500)
