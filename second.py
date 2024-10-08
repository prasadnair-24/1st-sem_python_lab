# Task: Write a Python program that:

# Asks the user for a number and checks if it is even or odd.
# Prints a message indicating whether the number is even or odd.

# Input from user
number = int(input("Enter a number: "))

# Check even or odd
if number % 2 == 0:
    print(f"{number} is even.")
else:
    print(f"{number} is odd.")
