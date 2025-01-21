from tkinter import *


def do_something(event):
    print(event)


app = Tk()

app.bind("<ButtonPress>", do_something)  # Apertar o botão
app.bind("<ButtonRelease>", do_something)  # Soltar o botão
app.bind("<Enter>", do_something)  # Passar por cima do elemento
app.bind("<Leave>", do_something)  # Sair de cima do elemento
app.bind("<Motion>", do_something)  # Pegar o movimento do mouse


app.mainloop()
