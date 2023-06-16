"""Simple error handling methods which prevent user error"""

#asks user for hours worked and handles any user error when numbers are not entered
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

#asks user for days worked and handles errors made by user when numbers are not entered
def get_days():
    """Method that will ask user for days worked and only accept int input"""
    #flag that will keep while loop running until user enters correct input
    flag = True
    while flag:
        try:
            days = int(input("Please enter number of days worked: "))
        except ValueError:
            print("Please enter a valid number.")
        else:
            flag = False
    return days

