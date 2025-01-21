import os
from tkinter import *
from tkinter import filedialog, colorchooser, font
from tkinter.messagebox import *
from tkinter.filedialog import *


def change_color():
    color = colorchooser.askcolor(title="pick a color or else")
    text_area.config(fg=color[1])


def change_font(*args):
    text_area.config(font=(font_name.get(), size_box.get()))


def new_file():
    app.title("Untitled")
    text_area.delete(1.0, END)


def open_file():
    file = askopenfilename(defaultextension=".txt", file=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    try:
        app.title(os.path.basename(file))
        text_area.delete(1.0, END)
        file = open(file, "r")
        text_area.insert(1.0, file.read())
    except:
        print("Error")
    finally:
        file.close()


def save_file():
    file = filedialog.asksaveasfilename(initialfile="unititled.txt",
                                        defaultextension=".txt",
                                        filetypes=[("All Files", "*.*"),
                                                   ("Text Documents", "*.txt")])
    if file is None:
        return
    else:
        try:
            app.title(os.path.basename(file))
            file = open(file, "w")
            file.write(text_area.get(1.0, END))
        except:
            print("Error")
        finally:
            file.close()


def cut():
    text_area.event_generate("<<Cut>>")


def copy():
    text_area.event_generate("<<Copy>>")


def paste():
    text_area.event_generate("<<Paste>>")


def about():
    showinfo(title="About this program", message="This is a program written by you.")


def quit():
    app.destroy()


app = Tk()
app.title("Text editor program")
file = None

# Início - Tamanho da Tela
app_width = 500
app_height = 500
screen_width = app.winfo_screenmmwidth()
screen_height = app.winfo_screenheight()

x = int((screen_width / 2) - (app_width / 2))
y = int((screen_height / 2) - (app_height / 2))

app.geometry("{}x{}+{}+{}".format(app_width, app_height, x, y))
# Fim - Tamanho da Tela

# Início - Font
font_name = StringVar(app)
font_name.set("Arial")

font_size = StringVar(app)
font_size.set("25")
# Fim - Font

# Início - Text area body
text_area = Text(app, font=(font_name.get(), font_size.get()))
scrool_bar = Scrollbar(text_area)
app.grid_rowconfigure(0, weight=1)
app.grid_columnconfigure(0, weight=1)
text_area.grid(sticky=N + E + S + W)
scrool_bar.pack(side=RIGHT, fill=Y)
text_area.config(yscrollcommand=scrool_bar.set)
# Fim - Text area body

# Início - Change color
frame = Frame(app)
frame.grid()
color_button = Button(frame, text="color", command=change_color)
color_button.grid(row=0, column=0)
# Fim - Change color

# Início - Change font
font_box = OptionMenu(frame, font_name, *font.families(), command=change_font)
font_box.grid(row=0, column=1)
# Fim - Change font

size_box = Spinbox(frame, from_=1, to=100, textvariable=font_size, command=change_font)
size_box.grid(row=0, column=2)

menu_bar = Menu(app)
app.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=quit)

edit_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Edit", menu=edit_menu)
edit_menu.add_command(label="Cut", command=cut)
edit_menu.add_command(label="Copy", command=copy)
edit_menu.add_command(label="Paste", command=paste)

help_menu = Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="Help", menu=help_menu)
help_menu.add_command(label="About", command=cut)

app.mainloop()
