from tkinter import *


def drag_start(event):
    widget = event.widget
    widget.startX = event.x
    widget.startY = event.y
    print("event.x: ", event.x)


def drag_motion(event):
    widget = event.widget
    x = widget.winfo_x() - widget.startX + event.x
    print(x, widget.winfo_x(), widget.startX, event.x)
    y = widget.winfo_y() - widget.startY + event.y
    widget.place(x=x, y=y)


app = Tk()
app.geometry("500x500")

label = Label(app, bg="red", height=5, width=10)
label.place(x=0, y=0)

label2 = Label(app, bg="blue", height=5, width=10)
label2.place(x=100, y=100)

label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)

label2.bind("<Button-1>", drag_start)
label2.bind("<B1-Motion>", drag_motion)
app.mainloop()
