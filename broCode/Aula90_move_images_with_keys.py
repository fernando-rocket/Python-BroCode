from tkinter import *

def move_right(event):
    label.place(x=label.winfo_x()+50, y=label.winfo_y())
def move_down(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()+50)
def move_up(event):
    label.place(x=label.winfo_x(), y=label.winfo_y()-50)
def move_left(event):
    label.place(x=label.winfo_x()-50, y=label.winfo_y())


app = Tk()
app.geometry("1200x700")
app.config(bg="white")

app.bind("<d>", move_right)
app.bind("<s>", move_down)
app.bind("<w>", move_up)
app.bind("<a>", move_left)

photo = PhotoImage(file="Aula90_carro_de_corrida.png")
label = Label(app, image=photo)
label.place(x=0, y=0)

app.mainloop()
