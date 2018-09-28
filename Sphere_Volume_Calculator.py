#GUI BASIC
import tkinter as tk
import math

def submit():

	print("Submit pressed")
	r = float(entr.get())
	v = math.pi*r*r*r*4/3
	v = round(v,3)
	output.config(state="normal")
	output.insert(tk.INSERT,v)

root = tk.Tk()
root.title("Volume of a cylinder")

labr = tk.Label(root, text = "Radius")
labr.pack()

entr = tk.Entry(root)
entr.pack()

btn = tk.Button(root, text="Submit", command=submit)
btn.pack()

output = tk.Text(root, width=50, height=10, borderwidth=2, relief=tk.GROOVE)
output.config(state="disabled")
output.pack()

root.mainloop()