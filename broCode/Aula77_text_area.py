from tkinter import *


def submit():
    print(textarea.get("1.0", END))


app = Tk()
textarea = Text(app,
                font=("Segoe Print", 60),
                width=10,
                height=4,
                bg="light yellow",
                padx=20,
                pady=20,
                fg="red")
textarea.pack()
Button(app, text="submit", command=submit).pack()
app.mainloop()
