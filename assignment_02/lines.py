# Danilo III O. Gonzales
# Problem Set 6: Lines of Codes

# Program Description
# Create a program that will count the number of lines, excluding blank lines and comments.

# Import sys module
import sys

# Validate number of command-line arguments
if len(sys.argv) < 2:                                   # Checks if user provided fewer than 1 argument (excluding the script name).
    sys.exit("Too few command-line arguments")          # Exits with message if missing filename.
elif len(sys.argv) > 2:                                 # Checks if more than one argument is provided.
    sys.exit("Too many command-line arguments")         # Exits with message if there are extra arguments.

# Check if the provided file is a Python file
if len(sys.argv) == 2 and sys.argv[1].endswith(".py"):  # Ensures there is one argument and it ends with ".py".
    try:
        with open(sys.argv[1]) as file:                 # Opens the specified Python file for reading.
            nlines = 0                                  # Initializes line counter to 0.
            for line in file:                           # Iterates over each line in the file.
                # Counts only lines that are not comments and not blank.
                if not line.lstrip().startswith("#") and line.strip() != "":
                    nlines += 1                         # Increments counter for valid lines.
            print(nlines)                               # Displays the total number of code lines.
    except FileNotFoundError:                           # Catches error if the specified file does not exist.
        sys.exit("File does not exist")                 # Exits with message if file cannot be found.
else:
    sys.exit("Not a Python file")                       # Exits if the provided argument is not a .py file.