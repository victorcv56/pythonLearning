"""Attempt to create a tip calculator"""
class tipCalculator:
    """tip calculator that will help make calculations based on tips made"""
    
    def __init__(self, hours_worked, days_worked, hourly_wage = 15.5):
        """constructor that takes tips, wage, and hours worked from user input"""
        
        self.tips = []
        self.hours_worked = hours_worked
        self.days_worked = days_worked
        self.hourly_wage = hourly_wage

    #need new function that will take days worked and weekly
    #hours to calculate $/hr
    def enter_tips(self):
        """Method fills list of tips with user input"""
        #logic that will fill list with user input and for loop
        #asking user for tips made each day 
        for i in range(self.days_worked):
            money = input("Tips made day %d: " % (i + 1))
            self.tips.append(money)

    def get_hourly(self):
        """calculate total made hourly with tips and wage"""
        #logic here needs to calculate how much mony /hr is made
        #using tip list, hours_worked, hourly_wage
        weekly_tips = 0
        for tip in self.tips: 
            weekly_tips += int(tip)
        
        return weekly_tips

    def get_weekly(self):
        """calculate tips made this week"""

        days_worked = input("How many days did you work this week: ")
        tips = 0
        for _ in range(int(days_worked)):
            tips_made = int(input("Enter tips made daily: "))
            tips += tips_made

        return int(tips)

