"""Practicing json module"""
import json

filename = "remember_me.json"
try:
    with open(filename) as f:
        username = json.load(f)
except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print("We'll remember you when you come back, {}".format(username))

else:
    print("Welcome back, {}".format(username))