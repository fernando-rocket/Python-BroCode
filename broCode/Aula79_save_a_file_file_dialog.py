from tkinter import *
from tkinter import filedialog


def save_file():
    file = filedialog.asksaveasfile(initialdir="C:\\Users\\Fernando\\Documents",
                                    defaultextension='.txt',
                                    filetypes=[
                                        ("Text file", ".txt"),
                                        ("Text file", ".html"),
                                        ("All files", ".*")
                                    ])
    if file is None:
        return
    #filetext = str(text.get(1.0, END))
    filetext = input("Enter some text I guess:")
    file.write(filetext)
    file.close()
    app.quit()


app = Tk()
Button(app, text="save", command=save_file).pack()
text = Text(app)
text.pack()
app.mainloop()
