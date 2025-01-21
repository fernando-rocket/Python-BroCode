from tkinter import *


def create_window():
    app2 = Tk()
    # app2 = Toplevel() --- faz com que caso a primeira janela seja fechada, essa fecha junto
    app.destroy()


app = Tk()
Button(app, text="create new window", command=create_window).pack()
app.mainloop()
