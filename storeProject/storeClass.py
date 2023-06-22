"""A simple class made to refactor my store project"""
import json
class gameInventory:
    """A simple class that will initialize a dictionary and different
    methods to manipulate it"""

    def __init__(self, filename):
        """Initialize a dictionary and pass number of games in inventory"""
        self.filename = filename
        self.games = {}
        
    #retrieves data from json file or creates a new one 
    def get_data(self):
        """
        New attempt at trying to open json file, if empty fill json file\n
        >>>Tries to open JSON, if null will
        create new json file if this works
        """
        try:
            with open(self.filename) as f:
                game_inventory = json.load(f)
        except FileNotFoundError:
            self.add_to_list()
            # with open(self.filename, 'w') as f:
            #     json.dump(f, game_inventory)
        
    #Create new json file when file is not found 
    def create_file(self):
        """If a list does not exist, will create new dicionary in json"""
        with open(self.filename, 'x') as f:
            json.dump(self.game_inventory)

    #Output file data for user 
    def see_inventory(self):
        """Method that will display current inventory available"""
        with open(self.filename) as f:
            print(json.load(f))
        
    #Add data to dictionary inside a for loop 
    def add_to_list(self):
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
            #self.game_inventory['game {}'.format] = {}
            self.games['game {}'.format]['name'] = name
            self.games['game {}'.format]['cost'] = cost
            self.games['game {}'.format]['price'] = price
            print(self.games)
    
        