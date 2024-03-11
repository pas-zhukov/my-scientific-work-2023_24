import numpy as np
import pandas as pd
from scipy.signal import argrelextrema
from matplotlib import pyplot as plt


class Measurements:
    def __init__(self, time, voltage, current):
        self.time = time
        self.voltage = voltage
        self.current = current
        self.size = len(self.time)

        self.max_voltage = max(voltage)
        self.min_voltage = min(voltage)
        if isinstance(current, pd.Series):
            if not current.empty:
                self.max_current = max(current)
                self.min_current = min(current)
        elif current:
            self.max_current = max(current)
            self.min_current = min(current)

    def get_voltage_extremes(self):
        if isinstance(self.voltage, pd.Series) or isinstance(self.voltage, pd.DataFrame):
            formatted_voltage = self.voltage.to_numpy()
        elif isinstance(self.voltage, list):
            formatted_voltage = np.array(self.voltage)
        elif isinstance(self.voltage, np.ndarray):
            formatted_voltage = self.voltage
        else:
            raise TypeError("Data format error!")

        maxes = argrelextrema(formatted_voltage, np.greater)
        mins = argrelextrema(formatted_voltage, np.less)
        extremes = [*maxes[0], *mins[0]]
        return extremes


class PotentiostatMeasurements(Measurements):
    def __init__(self, path_to_file: str):
        potentiostat_measurements = pd.read_csv(path_to_file, skiprows=25, sep="\t",
                                                names=["E(V)", "i(A/cm?)", "T(s)"], encoding='cp1251')
        potentiostat_seconds = [float(str(measure).split(' ')[0]) for measure in potentiostat_measurements["T(s)"]]
        potentiostat_voltage = potentiostat_measurements["E(V)"]
        potentiostat_current = potentiostat_measurements["i(A/cm?)"]
        super().__init__(potentiostat_seconds, potentiostat_voltage, potentiostat_current)