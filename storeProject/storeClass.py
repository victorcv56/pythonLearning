"""A simple class made to refactor my store project"""
import json_handling as jh
class gameInventory:
    """A simple class that will initialize a dictionary and different
    methods to manipulate it"""

    def __init__(self, filename):
        """Initialize a dictionary and pass number of games in inventory"""
        self.filename = filename
        self.games = {}
        #self.json_list = jh.retrieve_data(self.filename)
        #will try to steer away from json for now


    #Add data to dictionary inside a for loop 
    def add_to_list(self):
        """Want to add games to list without rewriting file, so maybe convert to 
        json string first then pass that string to file"""
        flag = True
        while flag:
            try: 
                game_count = int(input("\nHow many games would you like to add: "))
                if isinstance(game_count, int):
                    flag = False
            except ValueError:
                print("Please enter a number.")
        #for loop that will prompt user for info on item and save 
        #to dictionary
        if game_count > 0:
            for i in range(game_count):
        
                name = input("\nName of game: ")
                price = int(input("\nSelling for: "))
                cost = int(input("\nGame cost: "))
                #Easier access to nested keys
                #self.game_inventory = {}
                self.games['name'] = name
                self.games['cost'] = cost
                self.games['price'] = price
                print(self.games)
                #jh.save_list(self.filename, self.games)
                
                with open(self.filename, 'a') as f:
                    for key, value in self.games.items():
                        f.write("{} : {} \n".format(key, value))
                    f.write("\n")
        else:
            pass

    def to_pesos(self, cost):
        """Will convert dlls price to pesos"""
        pesos = cost / 16.5
        return pesos
    
    def total_spent(self):
        """Will parse thtough dictionary adding up all game prices"""
        print(len(self.json_list))
