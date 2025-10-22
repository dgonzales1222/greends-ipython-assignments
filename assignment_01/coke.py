# Danilo III O. Gonzales
# Introduction to Python
# Problem Set 2: Coke Machine

# Program Description
# In a file called "coke.py", implement a program that prompts the user to insert a coin
# one at a time, each time informing the user of the amount due.

# Conditions
# 1. The vending machine only accepts the following denominations: 25 cents, 10 cents, and 5 cents.
# 2. If the total amount of inserted coins is equal to or greater than 50 cents, the program displays
#    the change owed and terminates.

amount_due = 50  # Variable declaration and initialization for the amount due of one bottle of Coca-Cola in the vending machine

while amount_due > 0:  # The while loop continues to prompt for coins while the amount due is greater than 0.
    
    print(f"Amount due: {amount_due}")  # Displays the initial amount due, which is 50 cents.

    inserted_coin = int(input("Insert Coin: "))  # Prompts the user to insert a coin.

    if inserted_coin == 25 or inserted_coin == 10 or inserted_coin == 5:  # Checks if the inserted coin is an accepted denomination.
        amount_due -= inserted_coin  # Subtracts the value of the valid coin from the amount due.

amount_due = abs(amount_due)  # Uses the abs() function to get the absolute value of the amount due for the change owed.
print(f"Change Owed: {amount_due}")  # Displays the change owed once the amount due is 0 or less.