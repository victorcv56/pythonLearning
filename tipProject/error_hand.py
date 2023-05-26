"""Simple error handling methods which prevent user error"""

def get_hours():
    """Method that will take user input and check for errors"""
    flag = True#flag that will keep while loop running until user enters correct input
    while flag:
        try:
            hours = int(input("Enter number of hours worked: "))
        except ValueError:
            print("Please enter valid number.")
        else:
            flag = False
    return hours

def get_days():
    """Method that will ask user for days worked and only accept int input"""
    flag = True#flag that will keep while loop running until user enters correct input
    while flag:
        try:
            days = int(input("Please enter number of days worked: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            flag = False
    return days

