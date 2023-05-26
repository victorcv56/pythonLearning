import write_tips as write
"""Attempt to create a tip calculator"""
class tipCalculator:
    """tip calculator that will help make calculations based on tips made"""
    
    def __init__(self, hours_worked, days_worked, hourly_wage=15.5): 
        """Create a calculator that takes hours worked, days worked,
        and hourly wage in that order."""
        
        self.tips = []
        self.weekly_tips = 0
        self.hours_worked = hours_worked
        self.days_worked = days_worked
        self.hourly_wage = hourly_wage
        self.filepath = ''

    # def get_hours(self):#want this to ask for user input and handle user input error
    #     """Function that will check if hour input is integer"""
    #     #I have to instantiate class in order to use this functon which
    #     #does not work for what im trying to do...
    #     #unless i instantiate without arguments
    #     flag = True
    #     while flag:
    #         try: 
    #             hours = int(input("Hours worked this week: "))
    #         except ValueError:
    #             print("Enter a valid number")
    #         else: 
    #             flag = False #changes flag to stop loop
    #     return hours
    
    def enter_tips(self):
        """Method that will prompt user to enter tips made daily 
        based on days worked."""
        
        flag = True
        i = 1
        while flag:#loop that will only accept numbers as user input 
            print("Enter '0' to stop entering tips.")
            try:
                money = int(input("Tips made day {}: ".format(i)))
                self.tips.append(money)
            except ValueError:
                print("\nEnter only numbers.\n")
            else:
                i += 1
                if money == 0:
                    flag = False    
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
    