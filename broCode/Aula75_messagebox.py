from tkinter import *
from tkinter import messagebox


def click():
    while True:
        x = messagebox.askyesno(title="Info", message="Information")
        # lembre que tem outros "ask"
        print(x)
        if x:
            break
    messagebox.showinfo(title="Info", message="Information")
    messagebox.showerror(title="E", message="Error")
    messagebox.showwarning(title="W", message="Warning")


app = Tk()

button = Button(app, command=click, text="click me")
button.pack()

app.mainloop()
