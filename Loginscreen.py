import tkinter as tk

root = tk.Tk()
labid = tk.Label(root, text = "Student ID")
labid.pack()

entid = tk.Entry(root)
entid.pack()

butlgn = tk.Button(root, text = "submit")
butlgn.pack()

root.mainloop()