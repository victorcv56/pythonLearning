class Cards:
    """Create credit cards and manipulate them"""

    def __init__(self, bank, apr, owed):
        """initialize cards with bank name, apr, and amount owed"""
        self.bank = bank
        self.apr = apr
        self.owed = owed


    def interest_owed(self):
        """calculates interest paid for whole amount"""
        interest = (self.owed * (self.apr / 100) / 12) + (self.owed * .01)
        print(f"You will pay {interest} in monthly interest for this card")
        return int(interest)


