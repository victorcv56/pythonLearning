"""A set of classes used to represent gas and electric cars."""

class Car: #Parent Class 
    """A simple attempt to represent a car."""

    #method initializing car
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0


    #method organizing attributes in string
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""            
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    

    #method that will print out odometer reading
    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    #changes odometer attribute through this method
    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!!")

    #adds miles to odometer
    def increment_odometer(self, miles):
        """Add to odometer by amount entered by user"""
        self.odometer_reading += miles


