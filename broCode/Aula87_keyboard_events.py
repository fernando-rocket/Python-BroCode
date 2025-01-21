from tkinter import *


def do_something(event):
    print(event.keysym)
    print(event)
    print()
    label["text"] = f"{event.keysym}"


app = Tk()

label = Label(app, text="", font=("Arial", 50))
label.pack(expand=True)
app.bind("<KeyPress>", do_something)

app.mainloop()
