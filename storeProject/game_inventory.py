"""Simple attempt to make a dictionary of games in stock"""
import json

games_catalogue = {'Red Dead Redemption 2': {'cost':10.6, 'price':15},
                   'FF7': {'cost':10.6, 'price':20},
                   'Dragon Ball Kakarot': {'cost':10.6, 'price':15},
                   'God of War': {'cost':10.6, 'price':15},
                   'Greedfall': {'cost':10.6, 'price':12},
                   'WWE 2k23': {'cost':10.6, 'price':13},
                   'Re-Reckoning': {'cost':10.6, 'price':12}
                   }

def save_list(game_list, filename):
    """Saves list into filename given"""
    try:
        with open(filename, 'w') as f:
            json.dumps(game_list)
    except FileNotFoundError:
        filename = input("Name of file: ")
        with open(filename, 'w') as f:
            json.dumps(game_list)

def add_games(games_catalogue, game_list):
    num = int(input("How many games will you add: "))
    for i in range(num):
        name = input("\nName of game: ")
        #need to add logic to append new games to old list...
        game_list[name] = {}
        cost = float(input("\nHow much did game cost: "))
        price = float(input("\nHow much will you sell game for: "))
        game_list[name]['cost'] = cost
        game_list[name]['price'] = price
    new_dic = games_catalogue | game_list
    return new_dic
    
filename = input("Enter filename: ")
#save_list(games_catalogue, filename)
add_games()
save_list(games_catalogue, filename)
print(games_catalogue)