import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_simple.CSV'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #pobranie temp maksymalnej z pliku
    highs, dates, lows = [], [], []
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        high = int(row[5])
        low = int(row[6])
        dates.append(current_date)
        highs.append(high)
        lows.append(low)

#dane wykresu
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, highs, c='red', label= "Hottest")
ax.plot(dates,lows, c='blue', label= 'Collest')

#formatowanie wykresu
ax.set_title('Najwyzsza i najnizsza temperatra dnia, lipiec 2018', fontsize =24)
ax.set_xlabel('', fontsize=3)
ax.set_ylabel('Temperatura [F]', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()