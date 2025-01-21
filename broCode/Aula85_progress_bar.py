import time
from tkinter import *
from tkinter import ttk
import time


def start():
    while pro_bar['value'] < 100:
        time.sleep(0.01)
        pro_bar['value'] += 1
        percent = (pro_bar['value']/100)*100
        label['text'] = f"{percent:.0f}%"
        app.update()
    app.quit()


app = Tk()

pro_bar = ttk.Progressbar(app, orient=HORIZONTAL, maximum=100)
pro_bar.pack(pady=10)

label = Label(app, text="-%")
label.pack()

button = Button(app, text="download", command=start)
button.pack()

app.mainloop()
