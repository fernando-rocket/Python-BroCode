from tkinter import *
from time import sleep


class Ball:

    def __init__(self, canvas, x, y, diameter, xVelocity, yVelocity, color):
        self.canvas = canvas
        self.diameter = diameter
        self.xVelocity = xVelocity
        self.yVelocity = yVelocity
        self.image = canvas.create_oval(x, y, diameter+x, diameter+y, fill=color)

    def move(self):
        coordinates = canvas.coords(self.image)
        if coordinates[0] > WIDTH - self.diameter + 5 or coordinates[0] < 0:
            self.xVelocity *= -1
        if coordinates[1] > HEIGHT - self.diameter + 5 or coordinates[1] < 0:
            self.yVelocity *= -1
        canvas.move(self.image, self.xVelocity, self.yVelocity)
        app.update()
        sleep(0.01)


app = Tk()

WIDTH = 500
HEIGHT = 500

canvas = Canvas(app, width=WIDTH, height=HEIGHT, bd=1, relief=SOLID)
canvas.pack(expand=True)

volley_ball = Ball(canvas, 20, 20, 100, 8, 2, "white")
tennis_ball = Ball(canvas, 120, 120, 50, 2, 8, "yellow")
basket_ball = Ball(canvas, 300, 300, 190, 5, 10, "orange")
while True:
    volley_ball.move()
    tennis_ball.move()
    basket_ball.move()

app.mainloop()
