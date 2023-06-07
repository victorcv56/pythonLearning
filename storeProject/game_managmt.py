#6/7/23
#Made a mess, need to come back with better json and dictionary understanding,,
"""Practice even more for json"""
import json
video_games = {}
filename = 'game_catalogue.json'
games_bought = int(input("How many games did you buy? "))#i can use this variable to create new method(fill dictionary) 

#Method that will calculate the minimum price of games in order
#to make the money back.
def minimum_price():
    """Calculate the minimum price each game should sell to make profit"""
    money_spent = total_spent()
    #games_bought = int(input("How many games did you buy? "))#i can use this variable to create new method(fill dictionary) 
    ##NEED TO REFACTOR AND CLEAN CODE
    minimum = money_spent / games_bought
    fill_list(games_bought, video_games)
    #print(video_games)
    save_games(filename)
    see_games(filename, games_bought)
    return minimum

#Loop method that will end when user enters '0'. 
#Used to collect total spent on inventory
def total_spent():
    """Spits out total spent on games"""
    total = 0
    flag = True
    while flag:#while flag is true keep asking
        money = float(input("Please enter money spent on package(Enter 0 to end): "))
        total += money
        if money == 0:
            flag = False

    return total

#Loop that will fill dictionary with game information given by user.
def fill_list(games, list):
    """This will fill dictionary prompting user for game info"""
    flag = True
    name = input("Game name(enter 'q' to finish): ")
    price = input("Game price: ")
    while flag:
        list['game_name'] = name
        list['price'] = price
        name = input("Game name(enter 'q' to finish): ")
        if name == 'q':#when user wants to exit loop enter 'q' to change flag to false
            flag = False
        price = input("Game price: ")

#Try-except block to see if we can save to file, if not create new file.
def save_games(filename):
    """Will use json to save a file of games and their prices"""
    try:
        with open(filename, 'w') as f:
            json.dump(filename, f)
    except FileNotFoundError:
        print("File not found.")
    else:
        print("Saved info on file.")

def see_games(filename, games):
    """Will access json file and display info on game_list"""
    try:
        with open(filename) as f:
            game_list = json.load(f)

            #print the tipe of data variable
            print("Type:", type(game_list))

            #print data of dictionary
            for _ in range(games):
                print("\nGame: ", game_list['game_name'])
                print("\nPrice: ", game_stock['price'])

            return game_list
    except FileNotFoundError:
        print("File not found.")

# price = see_games()

game_stock = see_games(filename, games_bought)

print(game_stock)
#print("You will have to sell each game at {.2f}".format(price))
#Will create a program that will manage game store
#take oney spend, calculate how much games should
#be sold for and how much profit is made
