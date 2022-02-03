from tkinter import *

window = Tk ()
window.geometry ('700x500')
window.title ('Я как паравозик томас, иди нахуй хуесос')

def button1 ():
    res = "Привет {}".format(txt.get())  
    lbl.configure(text=res)

txt = Entry (window, width = 10)
txt.grid (column=0, row=2)

lbl = Label(window, text = "Хуесос)))", font = ('Lobster', 10))
lbl.grid (column = 0, row = 1)

btn = Button(window, text="Не нажимать!", bg='blue', fg='yellow', command=button1)
btn.grid (column=0, row=0)

window.mainloop ()