from random import choice

class RandomWalk():
    """Klasa przezmaczona do bladzenia losowego"""

    def __init__(self, num_points=5000):
        """Inicjalizacja atrybutow bladzenia"""
        self.num_points = num_points

        #początek układu wspolrzednych (0,0)
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Wygenerowanie wszystkich punktow dla bladzenia losowego"""

        #wykonywanie krokow az do osiagniecia oczekiwanej liczby punktow
        while len(self.x_values) < self.num_points:

            x_direction = choice([1, -1])
            x_distance = choice([0, 1, 2, 3, 4])
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice([0, 1, 2, 3, 4])
            y_step = y_direction * y_distance

            #odrzucanie ruchow prowadzcyh do nikad
            if x_step ==0 and y_step == 0:
                continue

            #ustalenie nastepnych wartosci Xi Y
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)