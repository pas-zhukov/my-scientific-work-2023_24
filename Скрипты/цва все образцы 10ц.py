import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

c10_91 = "../Измерения/20.12.23/097_cv.cor"
c10_94 = "../Измерения/20.12.23/094_cv.cor"
c10_99 = "../Измерения/20.12.23/099_cv.cor"
c10_103 = "../Измерения/20.12.23/103_cv.cor"
c10_175 = "../Измерения/06.02.24/175_cv_06.02.cor"
c10_181 = "../Измерения/06.02.24/181_CV_06.02.cor"

sample91 = PotentiostatMeasurements(c10_91)
sample94 = PotentiostatMeasurements(c10_94)
sample99 = PotentiostatMeasurements(c10_99)
sample103 = PotentiostatMeasurements(c10_103)
sample175 = PotentiostatMeasurements(c10_175)
sample181 = PotentiostatMeasurements(c10_181)


fig, ax = plt.subplots(1, 1, figsize=(10, 7))

per_cycle = 1800
s1 = per_cycle * 1
s2 = per_cycle * 11
current = list(map(lambda x: 1000 * x / 5, sample91.current))
ax.plot(sample91.voltage[-1800:-1], list(map(lambda x: 1000 * x / 5, sample91.current))[-1800:-1], color='cyan')
ax.plot(sample94.voltage[-1800:-1], list(map(lambda x: 1000 * x / 5, sample94.current))[-1800:-1], color='dodgerblue')
ax.plot(sample99.voltage[-1800:-1], list(map(lambda x: 1000 * x / 5, sample99.current))[-1800:-1], 'darkblue')
ax.plot(sample103.voltage[-1800:-1], list(map(lambda x: 1000  * x  /  5, sample103.current))[-1800:-1], color='orange')
ax.plot(sample175.voltage[-1800:-1], list(map(lambda x: 1000  * x  /  5, sample175.current))[-1800:-1], color='red')
ax.plot(sample181.voltage[-1800:-1], list(map(lambda x: 1000  * x  /  5, sample181.current))[-1800:-1], color='green')

# arrow = ax.arrow(0.39, 0.05, 0.04, 0.05, width=0.002)
# plt.annotate("cycle increase", (0.37, 0.05), (0.25, 0.05))

# ax.set_aspect(2)
#ax.set_title("Sample 091")

ax.set_xlabel(r"Потеницал образца, $В$", size=20)
ax.set_ylabel(r"Плотность тока, $мА/см^2$", size=20)

ax.tick_params(axis="both", direction="in", length=8, labelsize=16)

ax2 = ax.secondary_yaxis("right")
ax2.tick_params(axis="both", direction="in", length=8, labelcolor="white")
ax3 = ax.secondary_xaxis("top")
ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white")

ax.minorticks_on()
ax.tick_params(which='minor', direction='in', length=2)
ax.xaxis.set_minor_locator(plt.MultipleLocator(25))
ax.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax2.minorticks_on()
ax2.tick_params(which='minor', direction='in')
ax2.yaxis.set_minor_locator(plt.MultipleLocator(2.5))
ax3.minorticks_on()
ax3.tick_params(which='minor', direction='in')
ax3.xaxis.set_minor_locator(plt.MultipleLocator(25))

ax.set_xlim(-0.21, 0.7)
ax.set_ylim(-1, 1.2)

ax.legend(["Образец 91", "Образец 94", "Образец 99", "Образец 103", "Образец 175", "Образец 181"], fontsize=14)

# ax.grid()
fig.tight_layout()
fig.show()

fig.savefig("../Картинки/ЦВА/все образцы на 10 цикле.png", dpi=500)
