"""Using json module to read data from file saved previously"""
import json

filename = 'numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)