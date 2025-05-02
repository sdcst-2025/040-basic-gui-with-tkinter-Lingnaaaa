import tkinter as tk 
from tkinter import *
window=tk.Tk()
window.geometry("260x140")
window.title("Example")

dog=PhotoImage(file="dog.png")
label1=tk.Label(window,image=dog).place(x=50)
l1=tk.Label(window,text="Pochacco").place(x=120,y=40)
l2=tk.Label(window,text=" A cuddly little puppy! This is from the same \n creators who brought you Keropi and Kero Kero",bg="cyan")
l2.place(x=0,y=105)

window.mainloop()