from tkinter import *
from tkinter import filedialog
import os


def open_file():
    print("You've openned a file")


def save_file():
    print("You've saved a file")


def exit():
    app.quit()


def cut():
    print("You cut some text")


def copy():
    print("You copy some text")


def paste():
    print("You paste some text")


app = Tk()

image = PhotoImage(file="Aula80_image.png", width=30, height=30)

menubar = Menu(app)
app.config(menu=menubar)

fileMenu = Menu(menubar,
                tearoff=0,
                font=("MV Boli", 15))
menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=open_file, image=image, compound=LEFT)
fileMenu.add_command(label="Save", command=save_file, image=image, compound=LEFT)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit, image=image, compound=LEFT)

editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label="Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

app.mainloop()
