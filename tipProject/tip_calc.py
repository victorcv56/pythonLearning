"""Attempt to create a tip calculator"""
class tipCalculator:
    """tip calculator that will help make calculations based on tips made"""

    def __init__(self, tips_made, hourly_wage, hours_worked):
        """constructor that takes tips, wage, and hours worked from user input"""
        
        self.tips_made = tips_made
        self.hourly_wage = hourly_wage
        self.hours_worked = hours_worked

    def get_hourly(self):
        """calculate total made hourly with tips and wage"""

        hourly = (self.tips_made + (self.hourly_wage * self.hours_worked)) / self.hours_worked
        return int(hourly)
    
    def get_weekly(self):
        """calculate tips made this week"""

        days_worked = input("How many days did you work this week: ")
        tips = 0
        for _ in range(int(days_worked)):
            tips_made = int(input("Enter tips made daily: "))
            tips += tips_made

        return int(tips)

