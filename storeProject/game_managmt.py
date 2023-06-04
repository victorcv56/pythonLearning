"""Practice even more for json"""
import json

def total_spent():
    """Spits out total spent on games"""
    games = int(input("How many games did you buy? "))
    total = 0
    for _ in range(games):
        money = int(input("Please enter money spent on package: "))
        total += money

    return total

totalSpent = total_spent()
print(totalSpent)

#Will create a program that will manage game store
#take oney spend, calculate how much games should
#be sold for and how much profit is made
