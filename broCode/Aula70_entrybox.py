from tkinter import *


def submit():
    username = entry.get()
    entry.config(state=DISABLED)
    print("Hello,", username)


def delete():
    entry.delete(0, END)


def backspace():
    entry_lenght = len(entry.get())
    entry.delete(entry_lenght-1, END)


def show():
    if entry["show"] == "":
        entry["show"] = "*"
        show_btn["text"] = "show"
    else:
        entry["show"] = ""
        show_btn["text"] = "hide"


app = Tk()
entry = Entry(app,
              font=("Arial", 50),
              fg="#00FF00",
              bg="black"
              )
entry.insert(0, "SpongeBob")
entry.pack(side=LEFT)
submit_btn = Button(app, text="submit", command=submit)
submit_btn.pack(side=RIGHT)
delete_btn = Button(app, text="delete", command=delete)
delete_btn.pack(side=RIGHT)
backspace_btn = Button(app, text="backspace", command=backspace)
backspace_btn.pack(side=RIGHT)
show_btn = Button(app, text="hide", command=show)
show_btn.pack(side=RIGHT)
app.mainloop()
