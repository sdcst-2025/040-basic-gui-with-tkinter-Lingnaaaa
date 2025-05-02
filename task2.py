import tkinter as tk 
from tkinter import *
window=tk.Tk()
window.geometry("500x200")
window.title("T-Town Veterinary Clinic Database")
window.attributes('-topmost',True)

dog=PhotoImage(file="dog.png")
label1=tk.Label(window,image=dog)
label1.place(x=10,y=0)

search=tk.Button(window,text="Search by Name")
search.place(x=300,y=0)

search_borad=tk.Entry(window,text="Entry widgets can be typed in")
search_borad.place(x=400,y=5)

title=tk.Label(window,text="Client Database")
title.place(x=200,y=50)

name1=tk.Label(window,text="Name")
name1.place(x=25,y=110)
e1=tk.Entry(window,width=15).place(x=5,y=130)
n2=tk.Label(window,text="Type")
n2.place(x=140,y=110)
e2=tk.Entry(window,width=15).place(x=105,y=130)
n3=tk.Label(window,text="Breed")
n3.place(x=230,y=110)
e3=tk.Entry(window,width=15).place(x=205,y=130)
n4=tk.Label(window,text="Owner")
n4.place(x=330,y=110)
e4=tk.Entry(window,width=15).place(x=305,y=130)
n5=tk.Label(window,text="Birthdate")
n5.place(x=420,y=110)
e5=tk.Entry(window,width=15).place(x=405,y=130)

b1=tk.Button(window,text="<Previous").place(x=5,y=165)
b2=tk.Button(window,text="Save Entry").place(x=205,y=165)
b3=tk.Button(window,text="Next>").place(x=440,y=165)
window.mainloop()

