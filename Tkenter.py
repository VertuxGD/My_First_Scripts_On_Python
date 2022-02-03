from tkinter import *
from tkinter import messagebox

def btn_click ():
    print ('F')
    login = loginInput.get ()
    password = passField.get ()
    
    info_str = f'Данные: {str(login)}, {str(password)}'
    messagebox.showinfo (title="Название", message=info_str)
    
    #ашибка
    #messagebox.showerror (title="", message='Error 404')

root = Tk ()
root['bg'] = '#fafafa'
root.title ('Название программы')
root.wm_attributes ('-alpha', 1.0)
root.geometry ('500x350')

root.resizable (width=False, height=False)

canvas = Canvas (root, height=500, width=350)
canvas.pack ()
frame = Frame (root, bg='red')
frame.place (relx=0.15, rely=0.15, relwidth=0.7, relheight=0.7)

title = Label (frame, text='Говео, а не прогга =) ', bg='brown')
title.pack ()
btn = Button (frame, text='PRESS F', bg='green', command=btn_click)
btn.pack ()

loginInput = Entry (frame, bg='white')
loginInput.pack ()

passField = Entry (frame, bg='white', show='*')
passField.pack ()

root.mainloop ()