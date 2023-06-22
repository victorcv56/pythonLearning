import json
filename = 'game_catalogue.json'
games_catalogue = {}#empty dictionary for user to fill

#MONEY HANDLING
def individual_price(lot_price, num_games):
    """Calculate individual price for lots bought"""
    price = lot_price / num_games
    return price

#DATA HANDLING###
def retrieve_data(filepath):
    """Access json data and sabe it to new list variable"""
    try:
        with open(filepath) as f:
            list = json.load(f)
    except FileNotFoundError:
        with open(filepath, 'w') as f:
            json.dump(games_catalogue, f, sort_keys=True, indent= 4)#Learning python library
    return list

#MONEY HANDLING
def dlls_to_peso(dlls):
    """Convert dllr prices to pesos."""

#DATA HANDLING
def get_keys(game_list):
    """Access keys of dictionary to use them."""
    for i in range(len(game_list)):
        game_name = game_list.get(game_list)
        print(game_name)
    
#DATA HANDLING###
def add_games(game_list, filepath):
    """Want to add games to list without rewriting file, so maybe convert to 
    json string first then pass that string to file"""
    game_count = int(input("\nHow many games would you like to add: "))
    #for loop that will prompt user for info on item and save 
    #to dictionary
    for i in range(game_count):
        
        name = input("\nName of game: ")
        price = int(input("\nSelling for: "))
        cost = int(input("\nGame cost: "))
    #Easier access to nested keys
        game_list['game {}'.format(i + 1)] = {}
        game_list['game {}'.format(i + 1)]['name'] = name
        game_list['game {}'.format(i + 1)]['cost'] = cost
        game_list['game {}'.format(i + 1)]['price'] = price
        print(game_list)
    
    with open(filepath, 'w') as f:
        json.dump(game_list, f, indent=4)
    
#DATA HANDLING
def total_spent(game_list):
    """Want to access 'cost' keys to figure out how much i spent"""
    #intitialize a running total
    total = 0 
    for i in range(len(game_list)):
        cost = game_list['game {}'.format(i + 1)]['cost']
        total += cost

    return total

#DATA HANDLING
def total_gains(game_list):
    """Access the 'price' key to calculate total earnings"""
    total = 0
    for i in range(len(game_list)):
        gains = game_list['game {}'.format(i + 1)]['price']
        total += gains
    return total

new_data = retrieve_data(filename)

money_spent = total_spent(new_data)
print("You spent {} total".format(money_spent))
money_gained = total_gains(new_data)
print("You will earn {} total".format(money_gained))
gainz = money_gained - money_spent
print("You will make {} in profit if games sell at current price".format(gainz))

#Now i need to refactor code or create a class to make code cleaner
