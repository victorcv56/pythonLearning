"""A set of classes that can be used to represent electric cars."""
from car import Car 

class Battery():
    """A simple attempt to model a battery for an electric car"""
    def __init__(self, battery_size=75, battery_charge=100):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size
        self.battery_charge = battery_charge

    def describe_battery(self):
        """Print a statement describing battery size and charge"""
        print(f"This car has a {self.battery_size}-kWh battery at {self.battery_charge}%")

    def get_range(self):
        """Will display the range this battery provides"""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 125:
            range = 315
        
        print(f"This car can go about {range} miles on a full charge")


#Child class
class ElectricCar(Car): 
    """Different aspects of a car, especially for electric cars"""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class."""
        super().__init__(make, model, year)
        self.battery = Battery(125)