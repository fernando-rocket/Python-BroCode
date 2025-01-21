from tkinter import *
import time

app = Tk()

canvas = Canvas(app, height=500, width=500, bd=1, relief=SOLID)
canvas.create_line(0, 0, 500, 500, fill="blue", width=5)
canvas.create_line(0, 500, 500, 0, fill="red", width=5)
canvas.create_rectangle(50, 50, 250, 250, fill="greenyellow")
points = [200, 0, 500, 450, 0, 300]  # usando uma lista
canvas.create_polygon(points, fill="yellow", outline="red", width=5)
canvas.create_arc(0, 0, 500, 500,
                  fill="#D6FFA0",
                  style=PIESLICE,
                  start=300,
                  extent=300)
# esse start mexe no ângulo
# styles = PIESLICE, CHORD, ARC
canvas.pack(expand=True)

app.mainloop()
