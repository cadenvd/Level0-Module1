"""
* Write a python program that asks the user a minimum of 3 riddles.

* You can look at riddles.com if you don't already know any riddles.

* Collect the response of each riddle from the user and compare their
  answers to the correct answer. 

* Use a variable to keep track of the correctly answered riddles

* After all the riddles have been asked, tell the user how many they got
  correct
"""
from tkinter import messagebox, simpledialog, Tk

x = simpledialog.askstring(title=None, prompt="What is the next number in the sequence? 2, 3, 5, 9, 17, _")
if x == 33:
    a = x
y = simpledialog.askstring(title=None, prompt="I make two people out of one. What am I?")
if y == "mirror":
    b = y
z = simpledialog.askstring(title=None, prompt="Mr. and Mrs. Mustard have six daughters and each daughter has one brother. How many people are in the Mustard family?")
if z == "9":
    c = z
d = (a + b + c)

print("you got" ,d, "correct")
