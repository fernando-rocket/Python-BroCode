from tkinter import *

def move_right(event):
    canvas.move(photo_canvas, +10, 0)
def move_down(event):
    canvas.move(photo_canvas, 0, +10)
def move_up(event):
    canvas.move(photo_canvas, 0, -10)
def move_left(event):
    canvas.move(photo_canvas, -10, 0)


app = Tk()
app.geometry("1200x700")
app.config(bg="white")

app.bind("<d>", move_right)
app.bind("<s>", move_down)
app.bind("<w>", move_up)
app.bind("<a>", move_left)

canvas = Canvas(app, width=500, height=500)
canvas.pack()

photo = PhotoImage(file="Aula90_carro_de_corrida.png")
photo_canvas = canvas.create_image(0, 0, image=photo, anchor=NW)

app.mainloop()
