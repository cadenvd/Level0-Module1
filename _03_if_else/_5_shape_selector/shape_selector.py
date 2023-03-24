import turtle
from tkinter import messagebox, simpledialog, Tk

# Goal: Write a Python program that asks the user whether they want to
#       draw a triangle, square, or circle and then draw that shape.

if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    
    # Make a new turtle
    tu = turtle.Turtle()
    # Ask the user what shape they want to draw and store it in a variable
    shape = simpledialog.askstring(title=None, prompt="triangle, square, or circle")
    # Draw the shape requested by the user using if-elif-else statements
    if shape == "triangle":
        tu.circle(180, 360, steps=3)
    elif shape == "square":
        tu.circle(180, 360, steps=4)
    elif shape == "circle":
        tu.circle(180)
    # Call the turtle .done() method
    tu.done()
    window.mainloop()
