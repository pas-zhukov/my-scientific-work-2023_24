import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/06.02.24/175_cv_06.02.cor"

sample = PotentiostatMeasurements(cor_file)

fig, ax = plt.subplots(1, 1, figsize=(10, 7))

per_cycle = 1800
s1 = per_cycle * 1
s2 = per_cycle * 11
current = list(map(lambda x: 1000 * x / 5, sample.current))
# ax.plot(sample.voltage[:s1], current[:s1], 'c-')
ax.plot(sample.voltage[-per_cycle:], current[-per_cycle:], 'r-')

# arrow = ax.arrow(0.39, 0.05, 0.04, 0.05, width=0.002)
# plt.annotate("рост № цикла", (0.37, 0.05), (0.25, 0.05))

ax.set_aspect(1)
#ax.set_title("Sample 091")

ax.set_xlabel(r"Sample potential, $V$", size=28)
ax.set_ylabel(r"Current density, $mA/cm^2$", size=28)
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
ax.set_ylim(-0.21, 0.4)

# ax.grid()
fig.tight_layout()
plt.show()

fig.savefig("../ЦВА 175", dpi=500)
