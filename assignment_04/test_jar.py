# Danilo III O. Gonzales
# Problem Set 8: Cookie Jar

# Test Script for Problem Set 8
from jar import Jar
import pytest

# Test for __init__
def test_init():
    # Testing default initialization
    jar = Jar()
    assert jar.capacity == 12   # Check if the jar's maximum capacity is 12
    assert jar.size == 0        # Check if the jar is empty at the start (size == 0)

    # Test Value Errors given that all inputs must be a non-negative integer
    # Negative Cookie Value
    with pytest.raises(ValueError):
        Jar(-1)
    # Float Cookie Input
    with pytest.raises(ValueError):
        Jar(1.5)
    # String Cookie Input
    with pytest.raises(ValueError):
        Jar("12")

def test_str():
    jar = Jar()                                 # Initialize Jar
    assert str(jar) == ""                       # Check if the initialized Jar is empty
    jar.deposit(1)                              # Deposit 1 Cookie
    assert str(jar) == "🍪"                     # Check if there is a single cookie deposited
    jar.deposit(11)                             # Deposit 11 Cookie 
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"   # Check if there are 12 Cookies after depositing 11.
    jar.withdraw(4)                             # Withdraw 4 Cookie
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪"          # Check if there are only 8 cookies left after 4 cookies were withdrawn.
    jar.withdraw(8)                             # Withdraw the remaining 8 cookies.
    assert str(jar) == ""                       # Check if the jar is empty after withdrawing the remaining 8 cookies.   

def test_deposit():
    jar = Jar()                                 # Initialize Jar
    # Test deposit() by depositing 3 cookies
    jar.deposit(3)                              # Deposit 3 cookies
    assert jar.size == 3                        # Check if there are 3 cookies in the jar after deposit.
    # Maximize jar capacity by depositing 9 more cookies
    jar.deposit(9)                              # Deposit 9 more cookies
    assert jar.size == 12                       # Check if the jar is full after depositing 9 cookies
    # Deposit 1 more cookie to check what will happen if maximum capacity exceeds. Check if it raises a ValueError.
    with pytest.raises(ValueError):
        jar.deposit(1)
    # Check if negative value of deposit raises ValueError
    with pytest.raises(ValueError):
        jar.deposit(-1)

def test_withdraw():
    jar = Jar()                                 # Initialize jar
    jar.deposit(5)                              # Set the initial content of the jar to 5

    # Test withdraw() by withdrawing 2 cookies
    jar.withdraw(2)                             # Withdraw 2 cookies from the jar
    assert jar.size == 3                        # Check if there are 3 cookies remaining after withdrawing 2
    # Empty the jar
    jar.withdraw(3)                             # Withdraw the remaining 3 cookies.
    assert jar.size == 0                        # Check if the Jar is empty.
    # Check what will happen if we withdraw more than available. Check if it raises a ValueError.
    jar.deposit(2)                              # Deposit 2 more cookies (Current size == 2)
    with pytest.raises(ValueError):
        jar.withdraw(4)
    # Check if negative value of withdraw raises ValueError
    with pytest.raises(ValueError):
        jar.withdraw(-1)