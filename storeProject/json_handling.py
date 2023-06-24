import json
import os.path

def retrieve_data(filename):
    """retrieves json data or creates new json file."""
    game_inv = {}
    check_file = os.path.isfile(filename)
    try:
        if check_file:
            with open(filename) as f:
                game_inv = json.load(f)
        else:
            with open(filename, 'w') as f:
                json.dump(game_inv, f, indent=4)
    except FileNotFoundError:
        pass
    return game_inv

def save_list(filename, list):
    """saves information to json file"""
    with open(filename, 'a') as f:
        json.dump(list, f, indent=3)