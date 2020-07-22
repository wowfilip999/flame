import os
try:
    f = open("conf3.py")
except IOError:
    f = open("conf3.py", "w")
    f.write("import pyautogui\npyautogui.click()")

class legit:
  geo = ("180x100")

from tkinter import *
leg = Tk()
leg.configure(background="black")
leg.title("legitset")
leg.geometry(legit.geo)

def move():
 import os
 f = open("conf3.py", "w")
 f.write("print('test')")
 f.close()


test = Checkbutton(leg, bg="gray",text="move",fg="white",command=move,width=10)
test.pack()

leg.mainloop()
