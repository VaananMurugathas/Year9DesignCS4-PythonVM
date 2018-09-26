#GUI BASIC
import tkinter as tk
import math

def calculate():

	r = float(entr.get())



root = tk.Tk()
root.title("Volume of a cylinder")

labr = tk.Label(root, text = "Radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

output = tk.Text(root, width=50, height=10, borderwidth=2, relief=tk.GROOVE)

root.mainloop()