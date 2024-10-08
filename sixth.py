# Exercise 6: Basic Object-Oriented Programming
# Task: Create a simple class Student that:

# Has attributes for name and age.
# Includes a method to display the student's details.

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")

# Create a student instance
student1 = Student("Prasad Nair", 22)
student1.display_info()
