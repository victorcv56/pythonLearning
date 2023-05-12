from random import randint, choice
"""Classes using python random lib"""

class Lottery:

    def __init__(self): #constructor for lottery ticket
        """Initialize lottery object with list of numbers and letters"""
        
        self.lottery_letters = ['a', 'c', 'f', 'g', 'h', 't', 'w', 'l']#list with random letters
        self.lottery_numbers = []#empty list of numbers to be filled with fill_ticket function
        self.winning_ticket = []#empty list that will contain winning lottery number
        
        
    def fill_ticket(self):
        """Attempt to fill list(lottery ticket) with numbers and letters"""

        
        for i in range (0, 8):#for loop filling lottery_number list with random numbers
            i = randint(0, 10)
            self.lottery_numbers.append(i)

        
        for i in range (0,4):#for loop to fill winning_ticket list with random letters and numbers
            letter = choice(self.lottery_letters)
            self.winning_ticket.append(letter)
            number = choice(self.lottery_numbers)
            self.winning_ticket.append(number)
        
        
    def see_lottery_ticket(self): 
        """Displays winning lottery ticket number"""
        
        print(f"The winner of this week is lottery #: {self.winning_ticket}")

lot1 = Lottery()
lot1.fill_ticket()
#lot1.show_lottery()