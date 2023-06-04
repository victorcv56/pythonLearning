"""Favorite number 10-11"""
import json

def get_stored_num():
    """Asks user for favorite number and stores it"""
    try:
        filename = 'fave_num.json'
        with open(filename) as f:
            num = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return num

def get_new_num():
    """Asks for new number"""
    num = input("What is your fave number? ")
    filename = 'fave_num.json'
    with open(filename, 'w') as f:
            json.dump(num, f)

def say_num():
    """Looks for number and says it back to user"""
    num = get_stored_num()
    if num:
        print("Your favorite number is {}!".format( num))
    else:
        num = get_new_num()

say_num()