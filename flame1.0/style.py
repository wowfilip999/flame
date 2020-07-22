from tkinter import *
import os
style = Tk()
style.configure(background="black")
style.geometry("150x100")
style.title("style")

def color():
 co = Tk()
 co.configure(background="black")
 co.geometry("150x100")

 def cogray():
  f = open("conf2.py", "w")
  f.write("")

 co = Button(co,text="gray",command=cogray)
 co.pack()


 gray = Button(co,text="gray",command=color)
 co.mainloop()


color1 = Button(style,text="color",bg="gray",width=8,command=color)
color1.pack()

style.mainloop()
