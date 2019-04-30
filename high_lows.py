import csv
from datetime import datetime
from matplotlib import pyplot as plt

# Get high temperatures from file
filename = 'sitka_weather_2014.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    
    # Get current dates low and high temperatures from file
    dates, highs, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[0], '%Y-%m-%d')
        dates.append(current_date)
        high = int(row[1])
        highs.append(high)
        low = int(row[3])
        lows.append(low)
          
  
# Plot data
fig = plt.figure(dpi = 128, figsize = (10,6))
plt.plot(dates, highs, c='red')
plt.plot(dates, lows, c = 'blue')
plt.fill_between(dates, highs, lows, facecolor = 'blue', alpha=.1)

# Format plot
plt.title("Daily High & Low temperatures - 2014", fontsize = 24)
plt.xlabel('', fontsize = 16)
fig.autofmt_xdate()
plt.ylabel('Temperature(F)', fontsize = 16)
plt.tick_params(axis = 'both', which = 'major', labelsize = 16)

plt.show()
