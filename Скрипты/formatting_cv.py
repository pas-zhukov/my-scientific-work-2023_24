import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/20.12.23/097_cv.cor"
result_file = "../Измерения/По образцам/CV/091/Цикл 10.xlsx"

sample = PotentiostatMeasurements(cor_file)

fig, ax = plt.subplots(1, 1, figsize=(30, 30))

r1 = -1800
r2 = -1

ax.plot(sample.voltage[r1:r2], sample.current[r1:r2], 'r-')

data = {
    "T(s)": sample.time[r1:r2],
    "E(V)": sample.voltage[r1:r2],
    "i(A/cm?)": sample.current[r1:r2]
}
df = pd.DataFrame(data)


df.to_excel(result_file, index=False)


ax.grid()
fig.tight_layout()
fig.show()
fig.savefig("../test.png", dpi=500)