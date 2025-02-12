import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt

plt.rcParams['font.family'] = 'Arial'

from models import PotentiostatMeasurements

cor_file = "../Измерения/20.12.23/097_cv.cor"

sample = PotentiostatMeasurements(cor_file)

fig, ax = plt.subplots(1, 1, figsize=(10, 8))

per_cycle = 1800
s1 = per_cycle * 1
s2 = per_cycle * 11
current = list(map(lambda x: 1000 * x / 5, sample.current))
line1, = ax.plot(sample.voltage[:s1], current[:s1], 'c-', label="1'st cycle")
line2, = ax.plot(sample.voltage[s1:], current[s1:], 'b-', label="2-10 cycles")

arrow = ax.arrow(0.487, 0.0439, 0, 0.1, width=0.002, head_length=0.015, head_width=0.01, color="salmon")
arrow2 = ax.arrow(0.280, -0.007, 0, -0.125, width=0.002, head_length=0.015, head_width=0.01, color="salmon")
plt.annotate("cycle number", (0.3, 0.1488), (0.3, 0.1588), color="tomato", fontsize=20)
plt.annotate("       increase", (0.3, 0.1488), (0.3, 0.1449), color="tomato", fontsize=20)

# arrow3 = ax.arrow(0.212, 0.05, 0.023, -0.023, width=0.002, color="c")
# plt.annotate("1st cycle", (0.176, 0.055), (0.176, 0.055), color="c", fontsize=20)

ax.set_aspect(2)
#ax.set_title("Sample 091")

ax.set_xlabel(r"Sample potential, V", size=20)
ax.set_ylabel(r"Current density, mA/cm²", size=20)

# Увеличение толщины осей
for spine in ax.spines.values():
    spine.set_linewidth(2)

# Увеличение толщины тиков
ax.tick_params(axis="both", direction="in", length=8, labelsize=18, width=2)

# Добавление легенды с заголовком
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
ax.set_ylim(-0.15, 0.2)

# ax.grid()
fig.tight_layout()
plt.show()

fig.savefig("../Картинки/ЦВА/091 первые 10 циклов.png", dpi=500)