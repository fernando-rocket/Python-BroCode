from tkinter import *


def display():
    if x.get() == 0:
        print("OK")
    else:
        print("Not OK")


app = Tk()
photo = PhotoImage(file="Aula69_image.png")
x = IntVar()
checkbox = Checkbutton(app,
                       text="I agree to sth",
                       variable=x,
                       onvalue=0,
                       offvalue=1,
                       command=display,
                       font=("Arial", 20),
                       fg="#00FF00",
                       bg="black",
                       activeforeground="#00FF00",
                       activebackground="black",
                       padx=25,
                       pady=10,
                       image=photo,
                       compound=LEFT,
                       )
checkbox.pack()

app.mainloop()
