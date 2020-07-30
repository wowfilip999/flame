class size:
  a = ("1500x1500")
  b = ("black")


import os
import pyautogui
try:
    f = open("conf3.py")
except IOError:
    f = open("conf3.py", "w")
    f.write("import pyautogui")
    f.close()


class legit:
  geo = ("1500x1500")

from tkinter import *
leg = Tk()
leg.configure(background="black")
leg.title("legitset")
leg.geometry(size.a)


def reset():
 os.remove("conf3.py")
 f = open("conf3.py", "w")
 f.write("import pyautogui")
 f.close()


def move():
 f = open("conf3.py", "w")
 f.write("pyautogui.move(1, 1)")
 f.close()


def speed():
 speed = Tk()
 speed.geometry(size.a)
 speed.configure(background=size.b)
 speed.title("legit")


 def sp1():
  import os
  f = open("conf3.py", "a")
  f.write("\npyautogui.click()")
  f.close()

 def sp2():
  import os
  f = open("conf3.py", "a")
  f.write("\npyautogui.click(clicks=4)")
  f.close()



 nn = Label(speed,text="settings",bg="black")
 n = Button(speed,text="11 cps",bg="gray",width=45,height=3,borderwidth=3,command=sp1)
 nnn = Button(speed,text="16 cps",bg="gray",width=45,height=3,borderwidth=3,command=sp2)


 reset.pack()
 n.pack()
 nnn.pack()

 speed.mainloop()


tt = Label(leg, bg="black",text="legit settings",fg="red",height=5,font="italic")
reset = Button(leg, bg="gray",text="reset",fg="black",width=45,borderwidth=3,height=3,command=reset)
test = Button(leg, bg="gray",text="move",fg="black",command=move,width=45,borderwidth=3,height=3)
clickspeed = Button(leg, bg="gray",text="speed",fg="black",command=speed,width=45,borderwidth=3,height=3)



tt.pack()
test.pack()
clickspeed.pack()
reset.pack()
leg.mainloop()
