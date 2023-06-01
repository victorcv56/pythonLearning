"""Using json module to save data"""
import json

numbers = [1, 2, 4, 7, 34, 12]

filename = 'numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers, f)
