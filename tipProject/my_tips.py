"""Simple attempt to create weekly tips list"""
from calcClass import tipCalculator as tc
import error_hand as eh

hours = eh.get_hours()#calls on error handling class to only accept numbers
days = eh.get_days()#calls on error handling class to only accept numbers

week1 = tc(int(hours), int(days))
week1.enter_tips()

file1 = week1.log_tips()
week1.log_info()
#week1.log_info()#logging 0 total tips
#Have to fix log_info() method in order to be able to log more information 
#into txt file provided