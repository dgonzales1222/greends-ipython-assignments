# Danilo III O. Gonzales
# Introduction to Python
# Problem Set 2: Vanity Plates

# Program Description
# In a file called "plates.py", implement a program that prompts the user for a vanity plate
# and then outputs "Valid" if it meets all the requirements or "Invalid" if it does not.

# Conditions / Requirements
# 1. All vanity plates must start with at least two letters.
# 2. Vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
# 3. Numbers cannot appear in the middle of a plate; they must come at the end.
#    - Example: "AAA222" is acceptable, while "AAA22A" is not.
#    - The first number used cannot be '0'.
# 4. No periods, spaces, or punctuation marks are allowed.

def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    # In this problem, all rules must be true to consider the vanity plate inputted by the user Valid.
    # Any violation of the set conditions will render an Invalid plate.
    # In this problem, we can simplify condition 1, 2, and 4 in a conditional statement.
    # For condition 1, we can slice the first two characters and then use .isalpha() method to check if they are alphabet.
    # For condition 2, we can use the len() function and comparison operators to check if the character is within 2-6 characters.
    # For condition 4, we can use the .isalnum() method to determine if the plate consists of alphanumeric characters

    if s[0:2].isalpha() and len(s) <= 6 and len(s) >= 2 and s.isalnum():
        # If the string passes the initial conditions, proceed to check Condition #3.
        first_number_checker = False  # Tracks whether the first numeric character has been detected.

        for i in s:
            if i.isdigit():
                if not first_number_checker:  # If this is the first numeric character found
                    if int(i) == 0:  # If the first number is 0, the plate is invalid.
                        return False
                first_number_checker = True  # Marks that a numeric character has been found.
            else:
                if first_number_checker:  # If a letter appears after a number, the plate is invalid.
                    return False

        return True  # If the for loop completes without returning False, Condition #3 is satisfied. The plate is valid.
    else:
        return False #If the inputted plate number does not satisfy conditions 1, 2, and 4, it is invalid.

main()