try:
    import pyautogui
except ImportError:
    from tkinter import *
    from tkinter import messagebox
    root = Tk()
    root.title("Flame")
    messagebox.showwarning(" :-(", "pyautogui not installed but need in this aplication ")
    import os
    os.system("python3 install.py")
