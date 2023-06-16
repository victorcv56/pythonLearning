"""Simple attempt to create weekly tips list"""
from calcClass import tipCalculator as tc
import error_hand as eh

hours = eh.get_hours()#calls on error handling class to only accept numbers
days = eh.get_days()#calls on error handling class to only accept numbers

week1 = tc(int(hours), int(days))#create tips calculator object 
week1.enter_tips()

file1 = week1.log_tips()
week1.log_info()