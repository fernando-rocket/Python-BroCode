from tkinter import *
from time import sleep

WIDTH = 500
HEIGHT = 500
xVelocity = 8
yVelocity = 2

app = Tk()

canvas = Canvas(app, width=WIDTH, height=HEIGHT, bd=1, relief=SOLID)
canvas.pack(expand=True)

background_photo = PhotoImage(file="Aula67_image.png")
background = canvas.create_image(0, 0, image=background_photo, anchor=NW)

photo = PhotoImage(file="Aula80_image.png")
photo_canvas = canvas.create_image(100, 250, image=photo, anchor=NW)
imgW = photo.width()
imgH = photo.height()

while True:
    coordinates = canvas.coords(photo_canvas)
    if coordinates[0] > WIDTH-imgW + 5 or coordinates[0] < 0:
        xVelocity *= -1
    if coordinates[1] > HEIGHT-imgH + 5 or coordinates[1] < 0:
        yVelocity *= -1
    print(coordinates)
    canvas.move(photo_canvas, xVelocity, yVelocity)
    app.update()
    sleep(0.01)

app.mainloop()
