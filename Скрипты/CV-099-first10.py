import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/20.12.23/099_cv.cor"

sample = PotentiostatMeasurements(cor_file)

fig, ax = plt.subplots(1, 1, figsize=(10, 7))

per_cycle = 1800
s1 = per_cycle * 1
s2 = per_cycle * 11
current = list(map(lambda x: 1000 * x / 5, sample.current))
ax.plot(sample.voltage[:s1], current[:s1], 'c-')
ax.plot(sample.voltage[s1:], current[s1:], 'b-')

arrow = ax.arrow(0.37, 0.2, 0.04, 0.25, width=0.002)
plt.annotate("cycle increase", (0.37, 0.2), (0.24, 0.2))

ax.set_aspect(0.5)
#ax.set_title("Sample 091")

ax.set_xlabel(r"Sample potential, $V$", size=20)
ax.set_ylabel(r"Current Density, $mA/cm^2$", size=20)

# ax.legend(["1 цикл", "2-10 циклы"])
# ax.ticklabel_format(style = 'plain')

ax.tick_params(axis="both", direction='in', length=8)

ax2 = ax.secondary_yaxis("right")
ax2.tick_params(axis="both", direction="in", length=8, labelcolor="white")
ax3 = ax.secondary_xaxis("top")
ax3.tick_params(axis="both", direction="in", length=8, labelcolor="white")

# ax.set_yticks([.0001 * i for i in range(-15, 30, 5)])
ax.set_xticks([.1 * i for i in range(-2, 8, 1)])
ax3.set_xticks([.1 * i for i in range(-2, 8, 1)])

ax.set_xlim(-0.21, 0.7)
ax.set_ylim(-0.5, 0.8)

# ax.grid()
fig.tight_layout()
fig.show()

fig.savefig("../Картинки/ЦВА/099 первые 10 циклов.png", dpi=500)
