from tkinter import *
from tkinter import ttk

app = Tk()
app.geometry("500x500")

notebook = ttk.Notebook(app)
notebook.pack(expand=True, fill=BOTH)
# Se colocar fill=X ou fill=Y
# preenche tudo no eixo escolhido
# se deixar sem o fill, fixa o notebook no centro

frame1 = Frame(notebook, borderwidth=5, relief=SOLID)
notebook.add(frame1, text="Frame 1")

frame2 = Frame(notebook, borderwidth=5, relief=SOLID)
notebook.add(frame2, text="Frame 2")

lista = [frame1, frame2]
for item in lista:
    Label(master=item, text="Fernando Góis Srmukznc",
          width=50, height=25).pack()

app.mainloop()
