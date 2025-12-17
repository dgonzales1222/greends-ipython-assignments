# Danilo III O. Gonzales
# Problem Set 8: Cookie Jar

# Program Description
# Implement a class called Jar with the following methods:
class Jar:                                  # Create a class Jar
    # Method #1: __init__ should create a cookie jar with the given capacity.
    # Capacity must be a non-negative integer; otherwise, __init__ must raise a ValueError.
    def __init__(self, capacity=12):
        # Detect if the input is a non-negative integer.
        if not isinstance(capacity, int) or capacity < 0:
            raise ValueError("Capacity must be a non-negative integer.")
        self._capacity = capacity           # Set the maximum number of cookies the jar can hold.
        self._size = 0                      # Start with an empty jar by setting size to 0.

    # Method #2: __str__ should return a str with n number of cookies
    def __str__(self):
        return "🍪" * self._size            # Return one cookie emoji per cookie in the jar.

    # Method #3: deposit should add n cookies. If it exceeds capacity, raise a ValueError.
    def deposit(self, n):
        # Detect if deposit value is non-negative and does not exceed capacity.
        if n < 0:
            raise ValueError("Invalid deposit")
        if self._size + n > self._capacity:
            raise ValueError("Cookie jar is full!")
        self._size += n

    # Method #4: withdraw should deduct n cookies.
    def withdraw(self, n):
        # Detect if the withdrawal value is non-negative and not more than the current size.
        if n < 0:
            raise ValueError("Invalid withdrawal")
        if n > self._size:
            raise ValueError("Not enough cookies to withdraw")
        self._size -= n

    # Method #5: capacity should return the cookie jar’s capacity.
    @property
    def capacity(self):
        return self._capacity

    # Method #6: size should return the number of cookies actually in the cookie jar, initially 0.
    @property
    def size(self):
        return self._size