import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = 'sitka_simple.CSV'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    #pobranie temp maksymalnej z pliku
    rains,dates = [] ,[]
    for row in reader:
        current_date = datetime.strptime(row[2], "%Y-%m-%d")
        place_name = row[1]
        station_name = row[0]
        try:
            rain = float(row[3])
        except ValueError:
            print(f"Brak danych dla {current_date}.")
        else:
            rains.append(rain)
            dates.append(current_date)

#dane wykresu
plt.style.use('seaborn')
fig, ax = plt.subplots()
ax.plot(dates, rains, c='red')


#formatowanie wykresu
ax.set_title(f'Opady deszczu , lipiec 2018 \n{place_name}, stacja {station_name}', fontsize =24)
ax.set_xlabel('', fontsize=3)
ax.set_ylabel('Opady [mm]', fontsize=16)
ax.tick_params(axis='both', which='major', labelsize=16)

plt.show()