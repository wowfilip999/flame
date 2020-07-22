class check:
  a = ("150x100")
  b = ("module checker")

from tkinter import *
check = Tk()
check.geometry("170x100")
check.title("?")
t = Label(check,text="check module installed?",bg="lightblue",fg="black")
b = Button(check,text="ok")
t.pack()
b.pack()
check.mainloop()
