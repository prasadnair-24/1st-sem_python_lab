# Exercise 4: Lists and Loops
# Task: Write a program that:

# Creates a list of the first 10 squares (0^2 to 9^2).
# Prints each square using a loop.

squares = [i ** 2 for i in range(10)]

# Print squares
for square in squares:
    print(square)
