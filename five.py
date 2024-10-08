# Exercise 5: File Handling
# Task: Write a Python program that:

# Reads a text file and counts the number of words in it.
# Outputs the word count.

def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Test the function (make sure to have 'sample.txt' in the same directory)
print("Number of words in file:", count_words('sample.txt'))
