import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/20.12.23/099_cv.cor"

sample = PotentiostatMeasurements(cor_file)

fig, ax = plt.subplots(1, 1, figsize=(10, 8))

per_cycle = 1800
s1 = per_cycle * 1
s2 = per_cycle * 11
current = list(map(lambda x: 1000 * x / 5, sample.current))
ax.plot(sample.voltage[:s1], current[:s1], 'c-')
ax.plot(sample.voltage[s1:], current[s1:], 'b-')

arrow = ax.arrow(0.487, 0.2, 0, 0.35, width=0.002, color="salmon")
arrow2 = ax.arrow(0.280, -0.007, 0, -0.47, width=0.002, color="salmon")
plt.annotate("cycle number increase", (0.3, 0.57), (0.3, 0.57), color="tomato")

arrow3 = ax.arrow(0.212, 0.14, 0.023, -0.023, width=0.002, color="c")
plt.annotate("1st cycle", (0.176, 0.15), (0.176, 0.15), color="c")

ax.set_aspect(0.5)
#ax.set_title("Sample 091")

ax.set_xlabel(r"Sample potential, $V$", size=20)
ax.set_ylabel(r"Current density, $mA/cm^2$", size=20)

# ax.legend(["1 цикл", "2-10 циклы"])
# ax.ticklabel_format(style = 'plain')

ax.tick_params(axis="both", direction="in", length=8, labelsize=18)

ax2 = ax.secondary_yaxis("right")
ax2.tick_params(axis="both", direction="in", length=8, labelcolor="white")
ax3 = ax.secondary_xaxis("top")
ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white")

ax.minorticks_on()
ax.tick_params(which='minor', direction='in', length=2)
ax.xaxis.set_minor_locator(plt.MultipleLocator(0.025))
ax.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax2.minorticks_on()
ax2.tick_params(which='minor', direction='in')
ax2.yaxis.set_minor_locator(plt.MultipleLocator(0.05))
ax3.minorticks_on()
ax3.tick_params(which='minor', direction='in')
ax3.xaxis.set_minor_locator(plt.MultipleLocator(0.025))

ax.set_xlim(-0.21, 0.7)
ax.set_ylim(-0.5, 0.8)

# ax.grid()
fig.tight_layout()
plt.show()

fig.savefig("../Картинки/ЦВА/099 первые 10 циклов.png", dpi=500)
