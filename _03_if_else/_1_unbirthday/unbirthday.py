
from tkinter import simpledialog, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()

    birthday = simpledialog.askstring(title=None, prompt="What is your birthday? (mm/dd)")
    if birthday == ("03/24"):
        print("happy birthday")
    else:
        print("happy unbirthday")
