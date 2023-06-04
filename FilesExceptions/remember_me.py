"""Practicing the json module"""
import json 

def get_stored_username():
    """Get stored username if file exists"""
    filename = 'username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username


def greet_user():
    """This function will greet user by name"""
    username = get_stored_username()
    if username:
        print("Welcome back, {}".format(username))
    else:
        username = input("What is your name? ")
        filename = 'username.json'
        with open(filename, 'w') as f:
            json.dump(username, f)
            print("We'll remember you next time, {}".format(username))


greet_user()