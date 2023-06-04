"""Dictionary class of cards and method to manipulate list"""

class CardList:
    
    def __init__(self):
        """Constructor method that creates an empty dictionary"""
        self.card_list = {}

    def fill_list(self, key, value):
        """Method that will be used to fill dictionary with different cards"""
        self.card_list['key'] = value
        #this will add new key value pairs to dictionary
        #but am i going to need new dictionaries since