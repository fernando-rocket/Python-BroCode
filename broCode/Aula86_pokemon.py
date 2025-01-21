from tkinter import *

app = Tk()

canvas = Canvas(app, height=500, width=500, bd=1, relief=SOLID)

canvas.create_arc(0, 0, 500, 500,
                  fill="red",
                  extent=180,
                  width=10)
canvas.create_arc(0, 0, 500, 500,
                  fill="white",
                  extent=180,
                  start=180,
                  width=10)
canvas.create_oval(190, 190, 310, 310, fill="white", width=10)

canvas.pack(expand=True)
app.mainloop()
