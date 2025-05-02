import tkinter as tk 
window=tk.Tk()
window.title("tk")
window.geometry("320x25")

entry1 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry2 = tk.Entry(window,text="Entry widgets can be typed in", width=10)
entry3 = tk.Entry(window,text="Entry widgets can be typed in", width=20)
label1 = tk.Label(window,text="x",width=2)
label2 = tk.Label(window,text="=",width=2)
label1.grid(row = 1, column = 2)
label2.grid(row = 1, column = 4)
entry1.grid(row = 1, column = 1, padx=5)
entry2.grid(row = 1, column = 3)
entry3.grid(row = 1, column = 5, padx=5)



window.mainloop()
