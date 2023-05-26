import write_tips as write
"""Attempt to create a tip calculator"""
class tipCalculator:
    """tip calculator that will help make calculations based on tips made"""
    
    def __init__(self, hours_worked, days_worked, hourly_wage = 15.5):
        """Create a calculator that takes hours worked, days worked,
        and hourly wage in that order."""
        
        self.tips = []
        self.weekly_tips = 0
        self.hours_worked = hours_worked
        self.days_worked = days_worked
        self.hourly_wage = hourly_wage
        self.filepath = ''

    def enter_tips(self):
        """Method that will prompt user to enter tips made daily 
        based on days worked."""
        #logic that will fill list with user input and for loop
        #asking user for tips made each day 
        for i in range(self.days_worked):
            money = input("Tips made day %d: " % (i + 1))
            self.tips.append(money)
        self.get_hourly()#calls get_hourly method to change total_tips

    def total_tips(self):
        """Method that will return total amount of tips made that week."""
        #logic here needs to calculate how much mony /hr is made
        #using tip list, hours_worked, hourly_wage
        for tip in self.tips: 
            self.weekly_tips += int(tip)
        
        return self.weekly_tips
    
    def get_hourly(self):
        """Averages wage/hr from tips made and hours worked this week."""
        #logic here needs to include hours worked during week, tips made in week
        #and will average out totals in order to return $ made per hour    
        hourly = (self.weekly_tips + (self.hourly_wage * self.hours_worked)) / self.hours_worked
        return hourly
    
    def log_tips(self):
        """Call on filewriter module to log weekly tips to new .txt file"""
        self.filepath = write.log_tips(self.tips, self.total_tips())
        #catched returned filepath name in order to save it 

    def log_info(self):
        """Method that will display all info provided by methods"""
        #calling methods inside class so no need to call them again
        write.write_info(self.filepath, self.get_hourly(self.weekly_tips), self.days_worked, 
                         self.hourly_wage, self.weekly_tips)
        
#need to figure out what else to add to this class to make it a funcitoning app
#Also want to make it a nice format in order to write to file weekly
#Automate it every end of week so i can keep track of tips