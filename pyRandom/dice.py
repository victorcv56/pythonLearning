"""Classes usign random lib from python"""
from random import randint, choice

class Dice:
    #constructor starting a dice with 6 sides
    def __init__(self, sides=6):
        self.sides = sides

    def roll_die(self):
        roll = randint(1, int(self.sides))
        print(f"You rolled a {roll}")

die1 = Dice()
die2 = Dice(10)
die3 = Dice(20)

for i in range(1, 11):
    die3.roll_die()