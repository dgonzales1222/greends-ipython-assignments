# Danilo III O. Gonzales
# Introduction to Python
# Problem Set 1: File Extensions

# Program Description
# In a file called "extensions.py", implement a program that prompts the user
# for the name of a file and then outputs the file’s media type based on its suffix.

# From the provided website about common media types, the following extensions and
# their corresponding MIME types are used:
# .gif → image/gif
# .jpg or .jpeg → image/jpeg
# .png → image/png
# .pdf → application/pdf
# .txt → text/plain
# .zip → application/zip

# Conditions
# 1. File extensions are case-insensitive (.PDF = .pdf = .PdF).
# 2. If the file extension is not in the list above, output "application/octet-stream".

# Prompt the user to enter the filename and store it in the variable "file".
file = input("Filename: ")

# Use str.strip() and str.lower() to clean and standardize the input before processing.
# The strip() method removes leading and trailing spaces (similar to the TRIM function in Excel),
# while the lower() method converts all letters to lowercase.
file = file.strip().lower()

# Conditional statements to check the file extension and output the appropriate MIME type.
# The .endswith() method is used to identify the file's suffix.
if file.endswith(".gif"):
    print("image/gif")
elif file.endswith(".jpg") or file.endswith(".jpeg"):  # Uses the OR operator since both have the same MIME type.
    print("image/jpeg")
elif file.endswith(".png"):
    print("image/png")
elif file.endswith(".pdf"):
    print("application/pdf")
elif file.endswith(".txt"):
    print("text/plain")
elif file.endswith(".zip"):
    print("application/zip")
else:
    print("application/octet-stream")
