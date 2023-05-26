"""Simple attempt to create credit card list and manipulate cc objects"""

class Cards:
    """Create credit cards and manipulate them"""
    
    #Initialize card object that will ask for bank name, 
    # annual rate, and amount owed.
    def __init__(self, bank, apr, owed):
        """initialize cards with bank name, apr, and amount owed"""
        self.bank = bank
        self.apr = apr
        self.owed = owed 
        
    
    #Method that will append new card object to existing object list
    def fill_list(self, card):
        """function to fill list of card objects"""
        self.card_list.append(card)
        

    def interest_owed(self):
        """calculates interest paid for whole amount"""
        interest = (self.owed * (self.apr / 100) / 12) + (self.owed * .01)
        print(f"You will pay {interest} in monthly interest for this card")
        return int(interest)
