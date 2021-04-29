import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/toronto_weather_2020.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high, and low temperatures from this file.
    #   Also, convert file's Fahrenheit value to Celsius.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')

        high_f = int(float(row[5]))
        low_c = int(float(row[6]))
        high_c = (high_f - 32) * (5 / 9)
        low_c = (low_c - 32) * (5 / 9)

        dates.append(current_date)
        highs.append(high_c)
        lows.append(low_c)

    # Plot the high and low temperatures.
    plt.style.use('ggplot')
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(dates, highs, c='red', alpha=0.5)
    ax.plot(dates, lows, c='blue', alpha=0.5)
    plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

    # Format plot.
    plt.title('Daily high and low temperatures in 2020', fontsize=24)
    plt.xlabel('', fontsize=10)
    fig.autofmt_xdate()
    plt.ylabel('Temperature (C)', fontsize=10)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()