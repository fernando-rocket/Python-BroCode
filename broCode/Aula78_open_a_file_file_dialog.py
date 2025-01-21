from tkinter import *
from tkinter import filedialog
import os


def openFile():
    filepath = filedialog.askopenfilename(initialfile=os.path.dirname(__file__),
                                          title="Open file okay?",
                                          filetypes=(("text files", "*.txt"),
                                                     ("all files", "*-*")))
    file = open(filepath, "r")
    print(file.read())
    file.close()


app = Tk()
Button(app, text="Open", command=openFile).pack()
app.mainloop()
