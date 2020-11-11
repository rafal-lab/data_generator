import matplotlib.pyplot as plt
from Bladznie_losowe.random_walk import RandomWalk

#tworzenie wilu bladzen losowych
while True:
    #przygotowanie i wyswoetlenie
    rw = RandomWalk(50_000)
    rw.fill_walk()

    #rysowanie
    plt.style.use('seaborn')
    fig, ax = plt.subplots()
    point_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolors='none' ,s=2)
    #podkreslenie pierwszego i ostatniego punktu bladzenia
    ax.scatter(0,0, c='pink', edgecolors='none', s=30)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=30)
    #ukrycie osi
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    ax.set_title("Bladzenie losowe", fontsize=14)
    plt.show()

    keep_running = input("Utworzyc kolejne bladzenie losowe? t/n: ")
    if keep_running == 'n':
        break