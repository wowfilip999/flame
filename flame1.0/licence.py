from tkinter import *
from tkinter import messagebox
licence = Tk()
licence.geometry("160x100")
licence.title("ok")


a = Label(licence,text="flame have gnu general public 3 licence",font="italic")
b = Checkbutton(licence,text="ok")
a.pack()
b.pack()

licence.mainloop()
