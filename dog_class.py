class Dog:
    """an attempt to create a dog object"""

    def __init__(self, name, age):
        """initialize dog name and attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """simulate dog sitting"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """simulate dog rolling over"""
        print(f"{self.name} has rolled over.")