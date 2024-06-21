import pandas as pd
import matplotlib.pyplot as plt

FILE_PATH = "./mesurements/Shikhalieva/гальвано никель 0.2 с.dat"


def main():
    measurements: pd.DataFrame = pd.read_csv(FILE_PATH, names=["sec", "mA", "mV"], skiprows=1, delimiter="\s\s\s")

    fig, ax = plt.subplots(2, 1, figsize=(10, 7))
    ax[0].plot(measurements["sec"], measurements["mA"])

    avg_secs = []
    electricity = []
    for i in range(len(measurements["sec"]) - 1):
        avg_secs.append(measurements["sec"][i] / 2 + measurements["sec"][i+1] / 2)
        electricity.append((electricity[i-1] if i > 0 else 0) + calculate_square(measurements["sec"][i], measurements["sec"][i+1], measurements["mA"][i], measurements["mA"][i+1]))
    ax[1].plot(avg_secs, electricity)

    fig.show()
    print("Полный интеграл: ", electricity[-1], "мА*с")


def calculate_square(x1, x2, y1, y2):
    return (x2 - x1) * y1 + 0.5 * (y2 - y1) * (x2 - x1)


if __name__ == '__main__':
    main()
