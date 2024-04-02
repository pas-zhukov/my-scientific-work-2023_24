import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from models import PotentiostatMeasurements

cor_file = "../Измерения/27.03.24/181_CA_T40-280s_27.03.cor"
result_file = "../Измерения/По образцам/CV/181/181 ХА Циклы 515-516.xlsx"

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