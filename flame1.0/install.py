from tkinter import *
check = Tk()
check.geometry("170x100")
check.title("?")

def yes():
 import os
 os.system("pip3 ")


def pip():
 import os
 os.system("pip3 install pyautogui")


t = Label(check,text="install module?",bg="lightblue",fg="black")
u = Button(check,text="ok",command=pip,width=7)

t.pack()
u.pack()


check.mainloop()
