def calculate_retirement(name, age):
    years_left = 65 - age
    retirement_year = 2026 + years_left
    print(name + " will retire in the year " + str(retirement_year))
calculate_retirement("Alice", 25)
calculate_retirement("Bob", 50)

""" 1. DEFINE the function first... the function expects two pieces of info name and age
2. CALL the function... the code will do nothing until you call it
"""

def temperature_converter(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius
today_celsius = temperature_converter(77)
print("Today's temperature in Celsius is: " + str(today_celsius))