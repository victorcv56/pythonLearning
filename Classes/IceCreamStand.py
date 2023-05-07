from Restaurant import Restaurant as r
"""Inherited restaurant classes for child class"""

class IceCreamStand(r):
    """Creating a child class from restaurant class"""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize attributes of parent class"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ['vanilla', 'chocolate', 'strawberry']

    def show_flavors(self):
        print("The different flavors we have are: ")
        for flavor in self.flavors:
            print(f"{flavor}")

