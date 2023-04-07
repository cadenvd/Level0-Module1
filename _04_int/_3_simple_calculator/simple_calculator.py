"""
* Write a Python program that asks the user for two numbers.

* Then ask the user if the would like to add, subtract, multiply, or divide.

* Use if-else statements to provide the desired math operation on the numbers
  and display the result.
"""

from tkinter import messagebox, simpledialog, Tk

x = simpledialog.askinteger(title=None, prompt="Give one number")
y = simpledialog.askinteger(title=None, prompt="Give one number")
z = simpledialog.askstring(title=None, prompt="add, subtract, multiply, or divide")

if z == "add":
    print(x + y)
if z == "subtract":
    print(x - y)
if z == "multiply":
    print(x * y)
if z == "divide":
    print(x / y)
