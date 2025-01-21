from tkinter import *


def submit():
    print(scale.get())


app = Tk()

scale = Scale(app,
              from_=100,
              to=0,
              length=600,
              orient=VERTICAL,
              font=("Consolas", 20),
              tickinterval=10,
              fg="#ff1c00",
              showvalue=0,
              resolution=5,
              troughcolor="#69eaff",
              bg="black"
              )
scale.pack()
scale.set((scale['from']-scale['to'])/2+scale['to'])
Button(app, text="submit", command=submit).pack()
app.mainloop()
