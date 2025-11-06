# Danilo III O. Gonzales
# Problem Set 3: Felipe's Taqueria

# Program Description
# In a file called taqueria.py, implement a program that enables a user to place an
# order, prompting them for items, one per line, until the user inputs control-d,

# Conditions
# 1. After each inputted item, display the total cost of all items inputted thus far,
#    prefixed with a dollar sign ($) and formatted to two decimal places.
# 2. Treat the user’s input case insensitively.
# 3. Ignore any input that isn’t an item.
# 4. Assume that every item on the menu will be titlecased.

# Initialize menu
menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
# Initialization of Total Cost of Order in float data type.
total = 0.00
# While loop condition set to True to continuously ask for order until the user
# explicitly tell the program to stop (by catching an EOFError)
while True:
    try:                                            # Start of try block to handle EOFError when user inputs Ctrl + D
        order = input("Item: ").title().strip()     # Ask the user for orders by inputting the menu item.
                                                    # .title() string method converts the input into titlecase.
        if order in menu:                           # Checks if the entered order matches a key in the menu dictionary.
            total += menu[order]                    # Adds the corresponding menu price to the running total.
            print(f"Total: ${total:.2f}")           # Displays the total cost formatted to two decimal places.
    except EOFError:                                # Catches the end-of-file signal (Ctrl + D) to stop the loop.
        break                                       # Exits the while loop when EOFError occurs.
