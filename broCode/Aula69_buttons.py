from tkinter import *

clicks = {"counter": 0}


def click():
    clicks["counter"] += 1
    print("You've clicked the button", clicks["counter"])


app = Tk()
photo = PhotoImage(file="Aula69_image.png", width=100, height=100)
button = Button(app,
                text="Click me!",
                command=click,
                font=("Comic Sans", 30),
                fg="#00FF00",
                bg="black",
                activeforeground="blue",
                activebackground="black",
                #state=ACTIVE or DISABLED,
                image=photo,
                compound="bottom")
button.pack()

app.mainloop()