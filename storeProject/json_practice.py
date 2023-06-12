import json
filename = 'test.json'

games_catalogue = {'Red Dead Redemption 2': {'cost':10.6, 'price':15},
                   'FF7': {'cost':10.6, 'price':20},
                   'Dragon Ball Kakarot': {'cost':10.6, 'price':15},
                   'God of War': {'cost':10.6, 'price':15},
                   'Greedfall': {'cost':10.6, 'price':12},
                   'WWE 2k23': {'cost':10.6, 'price':13},
                   'Re-Reckoning': {'cost':10.6, 'price':12}
                   }

def retrieve_data(filepath):
    try:
        with open(filepath) as f:
            list = json.load(f)
            
    except FileNotFoundError:
            with open(filepath, 'w') as f:
                json.dump(games_catalogue, f, sort_keys=True, indent= 3)#Learning python library
    return list

def add_to_list(new_data, filepath):
    """Want to create a funtion that will add to dictionary and add it to json"""
    name = input("Name of game: ")
    cost = input("Price of sale: ")
    price = input("Cost of game: ")
    
    new_data[name] = {}
    new_data[name]['cost'] = cost
    new_data[name]['price'] = price
    
    json.dump(new_data, filepath)
    print(new_data)
    

new_data = retrieve_data(filename)
print(new_data)
print(type(new_data))
add_to_list(new_data, filename)