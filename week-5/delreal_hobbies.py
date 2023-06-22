""" 
    Title: hobbies.py
    Author: Hannah Del Real
    Date: 21 June 2023
    Description: Demonstrating use of for of loops and if...else statements
"""

# Create a list of 5 hobbies
hobbies = ["drawing", "dancing", "cooking", "gaming", "baking"]

# Use a for loop to iterate over list of hobbies
for hobby in hobbies:
    print(hobby)

# Create a list of days of the week
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

# Use a for loop to iterate over days and add an if..else statement to display the day 
for day in days:
    # If day is a weekend, display a message indicating it is a day off and to enjoy hobbies
    if day == "Sunday":
        print(f"Today is {day}, your day off. You should go and enjoy your hobbies!")
    elif day == "Saturday":
        print(f"Today is {day}, your day off. You should go and enjoy your hobbies!")
    # If it is a weekday, display a message indicating a work day.
    else:
        print(f"Today is {day}, a work day. Good luck, you got this!")