from random import randint

class Die():
    """Class shows single die"""

    def __init__(self, num_sides=6):
        """Założenie ze kosc ma postac szescianu"""
        self.num_sides = num_sides

    def roll(self):
        """Zwrot wartosci z zakresu od 1 do num_sides"""
        return randint(1, self.num_sides)
