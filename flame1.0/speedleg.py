 from tkinter import *
 a = Tk()
 a.title()
 a.configure(background="black")
 a.geometry("1500x1500")


 textset = Label(a, text="legit settings",height=5,fg="red")
 clickset = Button(a, text="1",command=click,bg="gray")

 textset.pack()
 clickset.pack()

 a.mainloop()
