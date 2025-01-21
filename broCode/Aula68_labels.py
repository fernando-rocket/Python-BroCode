from tkinter import *

app = Tk()

photo = PhotoImage(file="C:\\Users\\Fernando\\PycharmProjects\\broCode\\Aula68_programmer.png")

label = Label(app,
              text="Garoto de Programa",
              font=("Arial", 40, "bold"),
              fg="#00FF00", bg="black",
              relief=RAISED,
              bd=10,
              padx=20,
              pady=20,
              image=photo,
              compound="left")
label.pack()

app.mainloop()
