import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Function to display Python introduction
def introduction():
    st.header("Welcome to Python Learning App ")
    st.write("""I have prepared a simple and effective way to learn python basics to adv easily
    just read and test these codes and learn
    """)
    st.write("by Midhun")

# Function to display Python basics
def python_basics():
    st.header("Python Basics")
    st.write("""Python is an easy-to-learn, powerful programming language. It has efficient high-level data structures
    and a simple but effective approach to object-oriented programming.
    """)
    
    st.subheader("1. Variables and Data Types")
    st.write("""Variables are used to store data in Python. They can hold different data types such as integers, strings, and booleans.""")
    st.code("""
# Example of variables
x = 10  # Integer
y = 3.14  # Float
name = "John"  # String
is_valid = True  # Boolean
print(x, y, name, is_valid)
    """)
    
    st.subheader("2. Operators")
    st.write("""Operators are used to perform operations on variables and values.""")
    st.code("""
# Arithmetic Operators
sum = 5 + 3  # Addition
product = 5 * 3  # Multiplication
division = 10 / 2  # Division

# Comparison Operators
is_equal = (5 == 5)  # True
is_greater = (10 > 5)  # True
    """)
    
    st.subheader("3. Conditional Statements")
    st.write("""Conditional statements help in decision-making.""")
    st.code("""
# Example of if-else statements
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")
    """)

    st.subheader("4. Loops")
    st.write("""Loops help in executing a block of code multiple times.""")
    st.code("""
# Example of a for loop
for i in range(5):
    print("Iteration", i)

# Example of a while loop
x = 0
while x < 5:
    print("While loop iteration", x)
    x += 1
    """)

    st.subheader("5. Functions")
    st.write("""Functions help in reusing code by defining a block of code that can be called multiple times.""")
    st.code("""
# Example of a function
def greet(name):
    return "Hello " + name

print(greet("Alice"))
    """)

# Function to display Python advanced topics
def python_advanced():
    st.header("Advanced Python Topics")
    
    st.subheader("1. Object-Oriented Programming (OOP)")
    st.write("""OOP is a programming paradigm that uses objects and classes.""")
    st.code("""
# Example of a class in Python
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car: {self.brand} {self.model}")

# Creating an object
my_car = Car("Toyota", "Camry")
my_car.display_info()
    """)
    
    st.subheader("2. File Handling")
    st.write("""Python allows you to read and write files.""")
    st.code("""
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading from a file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
    """)
    
    st.subheader("3. Data Visualization")
    st.write("Using Matplotlib to plot a simple graph.")
    
    x = np.linspace(0, 10, 100)
    y = np.sin(x)
    fig, ax = plt.subplots()
    ax.plot(x, y, label='Sine Wave')
    ax.set_xlabel("X-axis")
    ax.set_ylabel("Y-axis")
    ax.set_title("Simple Plot in Python")
    ax.legend()
    st.pyplot(fig)

# Function to display Python projects and practice exercises
def python_projects():
    st.header("Practice Python with Mini Projects")
    st.write("""Practice makes perfect! Here are some small projects to reinforce your learning.""")
    
    st.subheader("1. To-Do List App")
    st.code("""
# Simple To-Do List in Python
tasks = []

def add_task(task):
    tasks.append(task)
    
add_task("Buy groceries")
add_task("Finish Python project")
print(tasks)
    """)
    
    st.subheader("2. Simple Calculator")
    st.code("""
# Basic Calculator in Python
def calculator(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b

print(calculator(10, 5, "add"))
    """)

# Main function to control the Streamlit app
def main():
    st.title("Learn Python with Ease!")
    st.sidebar.title("Navigation")
    option = st.sidebar.radio("Choose a Topic", ["Introduction", "Python Basics", "Advanced Python", "Practice Projects"])
    
    if option == "Introduction":
        introduction()
    elif option == "Python Basics":
        python_basics()
    elif option == "Advanced Python":
        python_advanced()
    elif option == "Practice Projects":
        python_projects()
    
if __name__ == "__main__":
    main()
