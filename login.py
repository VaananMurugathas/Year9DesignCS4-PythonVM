import tkinter as tk
from PIL import ImageTk
import PIL
from tkinter import *
import os

#VARIABLES
#Q:	How do I store data
#A:	Using a list and the append function is the way to go

#store all the passwords I generate 
password = [] #emprty list called password
#When I process I need to access each word
word1 = ""
outputStr = ""


#Step 1: I need to get the data from the fileds.
#To do this we add a button and we BIND a function

#FUNCTIONS
def submit():

	#Get values from entry boxes
	print("Submit Pressed")
	word1 = ent1.get()
	print(word1)
	#word2 = ent2.get()

	#Build an output string
	#To make a new line we use an escape code 
	outputStr = "Accessing VMurugathas Schedule"

	print(outputStr)

 
# root = Tk()
# img = PIL.Image.open("UCC.png")
# imglabel = Label(root, image = img)
# imglabel.grid(row = 1, column =0, columnspan = 2)
root = Tk()
img = ImageTk.PhotoImage(PIL.Image.open("UCC.png"))
panel = Label(root, image = img)
panel.grid(row = 1, column = 0, columnspan = 2)

titleLabel = tk.Label(root, text = "Schedule Maker", font=("Ariel", 16))
titleLabel.grid(row = 0, column = 0, columnspan = 2)

word1Label = tk.Label(root, text = "Student ID", font=("Ariel", 10), bg = "#FFFFFF")
word1Label.grid(row = 2, column = 0, sticky = "NESW")

ent1 = tk.Entry(root, bg = "#FFFFFF")
ent1.grid(row = 2, column = 1)

word2 = tk.Label(root, text = " ")

btnGo = tk.Button(root, text = "Login", font=("Ariel", 16), command = submit, bg = "#FFF9E8")
btnGo.grid(row = 3, column = 0, columnspan = 2, sticky = "NESW")



root.mainloop() 

