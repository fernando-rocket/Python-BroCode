from tkinter import *

app = Tk()
food = ["pizza", "hamburguer", "hotdog"]
photo = PhotoImage(file="Aula68_programmer.png")


def order():
    print(x.get())


x = IntVar()
for item in food:
    radiobutton = Radiobutton(app,
                              text=item,
                              variable=x,
                              value=food.index(item),
                              font=("Impact", 50),
                              image=photo,
                              compound=LEFT,
                              indicatoron=0,
                              width=600,
                              bg="black",
                              fg="#00FF00",
                              command=order
                              )
    radiobutton.pack(anchor=W)

app.mainloop()
