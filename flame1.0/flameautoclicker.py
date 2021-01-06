from tkinter import *

import pyautogui

root = Tk()
root.geometry("1500x1500")
root.title("Flame 1.0")
root.configure(background="black")


def warn():
 import os
 while True:
   os.remove("conf.py")


def minecraft():
 mc = Tk()
 mc.geometry("1500x1500")
 mc.configure(background="black")
 mc.title("Flame")



 def spam():
  import pyautogui
  import time

  time.sleep(5)
  f = open("spam.txt", "r")
  for word in f:
     pyautogui.press("t")
     pyautogui.typewrite(word)
     pyautogui.press("enter")
     pyautogui.typewrite(word)
     pyautogui.press("enter")




 def drop():
  import pyautogui
  import time
  while True:
    time.sleep(1)
    pyautogui.press("q")
    pyautogui.press("q")
    pyautogui.press("q")
    pyautogui.press("q")


 txt = Label(mc, fg="red",text="Flame",width=7,bg="black",font="italic")
 autodrop = Button(mc, fg="black",command=drop,text="autodrop",borderwidth=3,width=45,height=3,bg="gray")
 spam = Button(mc, fg="black",command=spam,text="spammer",borderwidth=3,width=45,height=3,bg="gray")

 txt.pack()
 autodrop.place(y=40,x=450)
 spam.place(y=110,x=450)
 mc.mainloop()



def test():
 from pynput.mouse import Button
 from pynput.keyboard import KeyCode
 delay = 0.001
 button = Button.left
 start_stop_key = KeyCode(char='s')
 exit_key = KeyCode(char='e')




def settings():
 import os
 os.system("python3 conf.py")
 set = Tk()
 set.configure(background="black")
 set.geometry("1500x1500")
 set.title("Flame")

 def legitset():
  os.system("python3 legitset.py")




 def legit():
  os.system("python3 timed.py")
  while True:
    os.system("python3 conf3.py")



 def mega():
  import pyautogui
  os.system("python3 timed.py")
  while True:
    pyautogui.click(clicks=17)


 def faster():
  os.system("python3 timed.py")
  while True:
    pyautogui.click(clicks=2)


 def fast():
  os.system("python3 timed.py")
  while True:
    pyautogui.click(clicks=5)


 def exit():
  root.destroy()


 def slow():
  os.system("python3 timed.py")
  while True:
    pyautogui.click()

 def test():
  import time
  os.system("python3 timed.py")
  while True:
    pyautogui.click()
    time.sleep(2)
    pyautogui.click()



 def timed():
  def op1():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(3)")

  def  op2():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(4)")

  def op3():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(5)")
  def op4():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(5)")

  def default():
   f = open("timed.py", "w")
   f.write("import time\ntime.sleep(2)")


  import time
  try:
      f = open("timed.py")
  except IOError:
        f = open("timed.py", "w")
        f.close()
  time.sleep(1)
  timed = Tk()
  timed.title("Flame")
  timed.configure(background="black")
  timed.geometry("1500x1500")

  jay = Label(timed, text="Flame 1.0",fg="red",bg="black",width=45,height=5)
  default = Button(timed, bg="gray",text="reset",command=default,width=45,borderwidth=3,height=3)
  option1 = Button(timed, bg="gray",text="3 sec",command=op1,width=45,borderwidth=3,height=3)
  option2 = Button(timed, bg="gray", text="4 sec",command=op2,width=45,borderwidth=3,height=3)
  option3 = Button(timed, bg="gray", text="5 sec",command=op3,width=45,borderwidth=3,height=3)
  jay.pack()
  default.pack()
  option1.pack()
  option2.pack()
  option3.pack()
  timed.mainloop()

 def moresettings():
  class set:
    a  = ("50x100")



  more = Tk()
  more.geometry("1500x1500")
  more.title("Flame")
  t = Button(more, text="legit")
  t.pack()

 def slowmore():
  print("test")


 text = Label(set,text="Flame 1.0",bg="black",fg="red",height=5)
 slow = Button(set,text="slow",bg="gray",command=slow,fg="black",borderwidth=3,width=45,height=3)
 faster = Button(set,text="faster",bg="gray",fg="black",command=faster,borderwidth=3,width=45,height=3)
 fast = Button(set,text="fast",bg="gray",fg="black",command=fast,borderwidth=3,width=45,height=3)
 mega = Button(set,text="mega",bg="gray",fg="black", command=mega,borderwidth=3,width=45,height=3)
 legit = Button(set,text="legit",bg="gray",fg="black",command=legit,borderwidth=3,width=45,height=3)
 timed = Button(set,text="timed",bg="gray",fg="black",command=timed,borderwidth=3,width=45,height=3)
 slowmore = Button(set,bg="gray",command=slowmore,height=3,width=0,borderwidth=1)



 text.pack()
 slow.pack()
 faster.pack()
 fast.pack()
 mega.pack()
 legit.pack()
 timed.pack()
 slowmore.place(y=90,x=844)



 set.mainloop()

def style():
 import os
 os.system("python3 style.py")



def info():
 a = ("20")
 info = Tk()
 info.configure(background="black")
 info.geometry("180x150")
 info.title("Flame")
 n = ("purple")
 inf = Label(info, text="Info:", bg="black", fg="red",width=a)
 version = Label(info, text="version 1.0 beta",fg=n,bg="black",width=a)
 dev = Label(info, text="dev Filip Šiller",fg=n,bg="black",width=a)
 module = Label(info, text="module pyautogui",fg=n,bg="black",width=a)
 contact = Label(info, text="Discord : filip999#2904",fg=n,bg="black",width=a)
 os = Label(info, text="your os : ubuntu",fg=n,bg="black",width=a)

 inf.pack()
 version.pack()
 dev.pack()
 module.pack()
 contact.pack()
 os.pack()

def help():
 help = Tk()
 help.geometry("1500x1500")
 help.configure(background="black")
 help.title("help")

 click = Label(help, text="CLICK",bg="black",fg="red",font="italic")
 clickinfo = Label(help, text="when press this button wiew click modes",bg="black",fg="red",font="arial")
 clickinfo2 = Label(help, text="modes:",bg="black",fg="red",font="arial")
 clickinfo3 = Label(help, text="click slow unknow cps",bg="black",fg="red",font="arial")
 click.place(x=5,y=40)
 clickinfo.place(x=5,y=70)
 clickinfo2.place(x=5,y=100)
 clickinfo3.place(x=5,y=130)
 help.mainloop()


def update():
 update = Tk()
 update.configure(background="black")
 update.geometry("1500x1500")
 update.title("flame")

 def browser():
  import requests

  url = "https://github.com/wowfilip999/flame"
  # just a random link of a dummy file

  r = requests.get(url)
  # retrieving data from the URL using get method

  with open("flame1.0.zip", 'wb') as f:

   f.write(r.content)
   # writes the URL contents from the server

 text = Label(update,text="updater",font="italic",fg="red",bg="black",height=5)
 t = Button(update,text="update",command=browser,width=45,borderwidth=3,height=2)

 text.pack()
 t.pack()

 update.mainloop()



text = Label(root, text="flame autoclicker",fg="red",bg="black",height=5,font="italic",cursor="cross")
click = Button(root, text="click",command=settings,fg="black",width=45,height=3,bg="gray",borderwidth=3,cursor="cross")
warn = Button(root, text="warn",command=warn,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
minecraft = Button(root, text="minecraft",command=minecraft,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
info = Button(root, text="info",command=info,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
update = Button(root, text="update",command=update,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
style = Button(root, text="style",command=style,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
exit = Button(root, text="exit",command=exit,bg="gray",fg="black",width=45,height=3,borderwidth=3,cursor="cross")
creator  = Label(root, text="by wowfilip999",bg="black",fg="red")
help  = Button(root, text="?",command=help,bg="white",fg="black",width=1,height=1,borderwidth=2)
text.pack()
click.pack()
warn.pack()
minecraft.pack()
info.pack()
update.pack()
style.pack()
exit.pack()
help.place(x=1250,y=670)
creator.place(x=5,y=670)

import os
os.chdir("extesions")
try:
    f = open("extesion.py")
    os.system("python3 extesion.py")
except IOError:
    warning = Label(root,text="no extesions loaded",fg="red",bg="black")
    warning.place(x=1100,y=675)



root.mainloop()
