"""Simple attempt to create weekly tips list"""
import tip_calc as calc

week1 = calc.tipCalculator(31, 4)
hourly = week1.enter_tips()
print(week1.get_hourly())