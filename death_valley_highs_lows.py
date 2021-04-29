import csv
from datetime import datetime

import matplotlib.pyplot as plt

filename = 'data/death_valley_2018_simple.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    # Get dates, high, and low temperatures from this file.
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], '%Y-%m-%d')
        try:
            high_f = int(row[4])
            low_f = int(row[5])
        except ValueError:
            print(f"Missing data for {current_date}")
        else:
            # Convert Fahrenheit value to Celsius
            high_c = (high_f - 32) * (5 / 9)
            low_c = (low_f - 32) * (5 / 9)

            dates.append(current_date)
            highs.append(high_c)
            lows.append(low_c)

# Plot high and low temperatures.
plt.style.use('ggplot')
fig, ax = plt.subplots(figsize=(10, 6))
ax.plot(dates, highs, c='red', alpha=0.5)
ax.plot(dates, lows, c='blue', alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor='blue', alpha=0.1)

# Format plot.
title = 'Daily high and low temperatures - 2018\nDeath Valley, CA'
plt.title(title, fontsize=20)
plt.xlabel('', fontsize=10)
fig.autofmt_xdate()
plt.ylabel('Temperature (C)', fontsize=10)
plt.tick_params(axis='both', which='major', labelsize=16)

plt.show()
