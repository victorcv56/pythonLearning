"""Practicing the json module"""
import json 


def greet_user():
    """This function will greet user by name"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("We'll remember you next time, {}".format(username))
    else:
        print("Welcome back, {}".format(username))

greet_user()