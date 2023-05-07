class User:
    """Attempt to create user profiles"""
    
    def __init__(self, first_name, last_name, age):
        """Initialize a new user taking 2 paramenters"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def describe_user(self):
        """Displays information on user"""
        print(f"First Name: {self.first_name} \nLast Name: {self.last_name} \nAge: {self.age}")
        
class Admin(User):
    """Create admin users with special privileges"""

    def __init__(self, first_name, last_name, age):
        """Initialize attributes for admin user"""
        super().__init__(first_name, last_name, age)
        self.privileges = Privileges()

    

class Privileges():
    """Create a list of privileges for admins"""

    def __init__(self):
        """Initialize privilege list for admin"""
        self.privileges = ["Can add users", "Can block users", "Can delete posts"]

    def show_privileges(self):
        for priv in self.privileges:
            print(priv)

user1 = Admin('gael', 'chavarria', 9)
user1.describe_user()
user1.privileges.show_privileges()