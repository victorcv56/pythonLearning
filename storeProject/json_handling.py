import json

def retrieve_data(filename):
    """retrieves json data and fills dictionary"""
    try:
        with open(filename) as f:
            game_inv = json.load(f)
    except FileNotFoundError:
        with open(filename, 'w') as f:
            json.dump(f, game_inv)

