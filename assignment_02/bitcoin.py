# Danilo III O. Gonzales
# Introduction to Python
# Problem Set 4: Bitcoin Price Index

# Program Description
# In a file called bitcoin.py, implement a program that:
# 1. Expects the user to specify as a command-line argument the number of Bitcoins, n,
# that they would like to buy. If that argument cannot be converted to a float, the program
# should exit via sys.exit with an error message; and
# 2. Queries the API for the CoinCap Bitcoin Price Index.
# 3. Compute and display total price of Bitcoin.

# Import sys module and requests library.
import sys
import requests

# Checking command line argument using sys.argv
if len(sys.argv) != 2:                                  # Checks if exactly one argument (besides the script name) is provided.
    sys.exit("Missing command-line argument")           # Exits if the argument is missing.

try:
    btc_input = float(sys.argv[1])                      # Converts the input argument to float.
except ValueError:
    sys.exit("Command-line argument is not a number")   # Exits if conversion to float fails.

# Get Bitcoin price
try:
    btc_coincap = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=208c40df11680badf2f4ea977d9fab5331114248c06cf406fd4de97a5154d19d")  # Sends GET request to CoinCap API.
    data = btc_coincap.json()                           # Converts the JSON response to a Python dictionary.
    price = float(data["data"]["priceUsd"])             # Extracts the current Bitcoin price in USD and converts it to float.
except requests.RequestException:
    sys.exit("API Request Error")                       # Exits the program if there is a network or request-related error.

# Compute and print total price
btc_price = btc_input * price                           # Multiplies the number of Bitcoins by the current price in USD.
print(f"${btc_price:,.4f}")                             # Displays the total cost formatted with commas and 4 decimal places.