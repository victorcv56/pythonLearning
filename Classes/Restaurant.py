"""Different classes used to represent a restaurant"""

class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant object with name and type of cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Displays restaurant name and cuisine type"""
        print(f"This restaurant's name is {self.restaurant_name}.")
        print(f"It serves {self.cuisine_type}-style food")

    def open_restaurant(self):
        """Prints out message that restaurant is now open"""
        print(f"{self.restaurant_name} is now open!")
