
# Write a Python program that asks the user for the radius of a circle.
import math
import turtle


from tkinter import simpledialog
window_width = 600
window_height = 600

aoc = math.pi
radius = simpledialog.askinteger(title=None, prompt="Give radius of a circle.")
# Next, ask the user if they would like to calculate the area or circumference of a circle.
circumference = simpledialog.askstring(title=None, promt="Would you like to calculate the area or circumference of a circle?")
# If they choose area, display the area of the circle using the radius.
if circumference == "area" or circumference == "Area" or circumference == "AREA":
    tur = turtle.Turtle
    tur.circle(radius)
    tur.write(arg="area = " + str(aoc), move=True, align='left', font=('Arial',15,'normal'))
else:
    print("Try again!")
# Otherwise, display the circumference of the circle using the radius.
if circumference == "circumference" or circumference == "Circumference" or circumference == "CIRCUMFERENCE":
    tur = turtle.Turtle
    tur.circle(radius)
    Circum = math.pi * radius * 2
    A = 2 * (math.pi * (radius**2))

#Area = πr^2
#Circumference = 2πr 
