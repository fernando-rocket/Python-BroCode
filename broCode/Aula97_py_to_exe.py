from tkinter import *
import datetime


def update_clock():
    hours = datetime.datetime.now().hour
    minutes = datetime.datetime.now().minute
    seconds = datetime.datetime.now().second
    clock["text"] = f"{hours}:{minutes}:{seconds}"
    day_of_week["text"] = f"{datetime.datetime.now().strftime("%A")}"
    date["text"] = f"{datetime.datetime.now().strftime("%B %d, %Y")}"
    app.after(1000, update_clock)

app = Tk()
print(datetime.datetime.now())

clock = Label(app, text="", fg="green", bg="black", font=("Arial", 50))
clock.pack(fill=X, expand=True)

day_of_week = Label(app, text="", font=("Arial", 50))
day_of_week.pack(fill=X, expand=True)

date = Label(app, text="", font=("Arial", 50))
date.pack(fill=X, expand=True)

update_clock()

app.mainloop()
