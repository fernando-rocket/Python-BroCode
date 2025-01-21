from tkinter import *
from time import sleep

app = Tk()
listbox = Listbox(app,
                  bg="black",
                  fg="#00FF00",
                  font=("Arial", 15),
                  selectmode=MULTIPLE)
listbox.config(height=listbox.size())
listbox.pack()


def submit():
    listbox['state'] = DISABLED
    #try:
        #print(listbox.get(listbox.curselection())) # aqui escolhe o item que está clicado
        # dá erro quando nada está clicado
    #except:
        #print("You didn't ordered anything")
    food = []
    for index in listbox.curselection():
        food.insert(index, listbox.get(index))
    print(food)
    sleep(0.8)
    app.quit()


def add():
    listbox.insert(END, entrada.get())
    entrada.delete(0, END)


def delete():
    #try:
        #listbox.delete(listbox.curselection())
    #except:
        #print("You didn't select anything")
    for index in listbox.curselection():
        listbox.delete(index)

entrada = Entry(app)
entrada.pack()
Button(app, text="submit", command=submit).pack()
Button(app, text="add", command=add).pack()
Button(app, text="delete", command=delete).pack()

app.mainloop()
