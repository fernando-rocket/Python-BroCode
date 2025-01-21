from tkinter import *
from tkinter import colorchooser


def click():
    color = colorchooser.askcolor()
    colorHex = color[1]
    app['bg'] = colorHex


app = Tk()
app.geometry("420x420")
Button(app, text="click me", command=click).pack()
app.mainloop()
