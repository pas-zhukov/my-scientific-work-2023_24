import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/28.02.24/091_CA_3cycles_T80s_100Hz_28.02.cor"
result_file = "../Измерения/По образцам/CV/091/Циклы 1022-1024 (ХА).xlsx"

sample = PotentiostatMeasurements(cor_file)

fig, ax = plt.subplots(1, 1, figsize=(50, 50))

r1 = 0
r2 = -1

ax.plot(sample.time[r1:r2], sample.current[r1:r2], 'rp')

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