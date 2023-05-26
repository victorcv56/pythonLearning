"""Simple attempt to create weekly tips list"""
from calcClass import tipCalculator as tc

hours = input("Hours worked this week: ")
days = input("Number of days worked this week: ")
week1 = tc(int(hours), int(days))
week1.enter_tips()
week1.log_tips()
week1.log_info()#logging 0 total tips