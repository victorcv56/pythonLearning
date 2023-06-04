"""Simple attempt to create credit cards as dictionaries and manipulate them"""

class Cards:
    """Create dictionary of individual cards and add info to them"""
    
    #Initialize card object that will ask for bank name, 
    # annual rate, and amount owed.
    def __init__(self):
        """initialize cards with bank name, apr, and amount owed"""
        self.card = {}

    def add_to_card(self, key, value):
        """Method that will add new key, value pairs to card"""
        self.card[key] = value
        
    def show_card(self, key):
        """Method that will print out dicitonary's contents"""
        val = self.card.get(key, 'value is not available')
        print(val)