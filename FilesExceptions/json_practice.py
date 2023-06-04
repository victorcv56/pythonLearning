"""Practicing json module"""
import json

def remember_name():
    """This module will remember and store a given string"""
    filename = "given_name.json"
    try: 
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        username = input("What is your name? ")
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("Got your name, {}".format(username))
    else:
        print("Welcome back, {}".format(username))

remember_name()