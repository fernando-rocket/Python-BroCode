from tkinter import *


def submit():
    print(
        f"""Name: {firstNameEntry.get()}
Lastname: {lastNameEntry.get()}
Email: {emailEntry.get()}""")
    for item in entries:
        item.delete(0, END)



app = Tk()

title = Label(app, text="Enter your info")
title.grid(column=0, row=0, columnspan=2)

firstNameLabel = Label(app, text="First name: ", bg="#D6FFA0")
firstNameEntry = Entry(app)
firstNameLabel.grid(column=0, row=1)
firstNameEntry.grid(column=1, row=1)

lastNameLabel = Label(app, text="Last name: ", bg="greenyellow", width=30)
lastNameEntry = Entry(app)
lastNameLabel.grid(column=0, row=2)
lastNameEntry.grid(column=1, row=2)

emailLabel = Label(app, text="Email: ", bg="#D6FFA0", width=25)
emailEntry = Entry(app)
emailLabel.grid(column=0, row=3)
emailEntry.grid(column=1, row=3)


entries = [firstNameEntry, lastNameEntry, emailEntry]

submit_btn = Button(app, text="Submit", command=submit)
submit_btn.grid(column=0, row=4, columnspan=2)

app.mainloop()
