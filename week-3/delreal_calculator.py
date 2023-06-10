""" 
    Title: delreal_calculator.py
    Author: Hannah Del Real
    Date: 7 June 2023
    Description: Create functions to calculate basic arithmetic.
"""

# Create a function to add two numbers
def add(num1, num2):
    return num1 + num2


# Create a function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2

# Create a function to divide two numbers
def divide(num1, num2):
    return num1 / num2

# Create a function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2

# Create variables with values to test functions
num_1 = 2
num_2 = 4
num_3 = 3
num_4 = 9

# Create variables that call functions using test variables
new_sum = "{} + {} is {}".format(num_1, num_2, add(num_1, num_2))
new_difference = "{} - {} is {}".format(num_4, num_2, subtract(num_4, num_2))
new_quotient = "{} / {} is {}".format(num_4, num_3, divide(num_4, num_3))
new_product = "{} * {} is {}".format(num_1, num_4, multiply(num_1, num_4))




# Output strings for each arithmetic function
print(new_sum)
print(new_difference)
print(new_quotient)
print(new_product)
