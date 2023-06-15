import json
filename = 'test.json'
games_catalogue = {}#empty dictionary for user to fill

def individual_price(lot_price, num_games):
    """Calculate individual price for lots bought"""
    price = lot_price / num_games
    return price

def retrieve_data(filepath):
    """Access json data and sabe it to new list variable"""
    try:
        with open(filepath) as f:
            list = json.load(f)
    except FileNotFoundError:
        with open(filepath, 'w') as f:
            json.dump(games_catalogue, f, sort_keys=True, indent= 3)#Learning python library
    return list

def dlls_to_peso(dlls):
    """Convert dllr prices to pesos."""


def add_to_list(game_list, filepath):
    """Want to create a funtion that will add to dictionary and add it to json"""
    # with open(filepath) as f:
    #     game_list = json.load(f)
    game_count = int(input("\nHow many games would you like to add? "))   
    for i in range(game_count):
        name = input("\nName of game: ")
        cost = int(input("\nSelling for: "))
        price = int(input("\nGame cost: "))
    
        game_list[name] = {}
        game_list[name]['cost'] = cost
        game_list[name]['price'] = price
    
    with open(filepath, 'w') as f:
        json.dump(game_list, f, indent=3)
    print(game_list)
    
lot1 = individual_price(62.94, 12)
print(lot1)
new_data = retrieve_data(filename)
add_to_list(new_data, filename)
