import tkinter as tk
from PIL import ImageTk
import PIL
from tkinter import *
import os

#Creates class which allows me to use same variables across the code
class Dayview:

	#A constructor is special method made when you first create an instance of class.  This method is ONLY RUN ONCE
	def __init__(self):
		# Reads from text file schedule.txt
		self.lines = [] 
		with open ('schedule.txt', 'rt') as in_file: 
			for self.line in in_file: 
				self.lines.append(self.line.rstrip("\n\r"))
		def weekview():
			print("Showing schedule")
			#destroys daily frame and creates weekly frame
			self.root.destroy()

			self.root2 = tk.Tk()	
			self.titlab = tk.Label(self.root2, text = "Full Schedule", font = ("Ariel", 16))
			self.titlab.grid(row = 0, column = 0, columnspan = 7)

			self.btnd = tk.Button(self.root2, text = "Daily", font=("Ariel", 9), command = createDayView, bg="#FFF9E8")
			self.btnd.grid(row = 0, column = 0)

			self.d1 = tk.Label(self.root2, text = "Day 1", font =("Ariel", 18))
			self.d1.grid(row = 1, column = 0, columnspan = 2)

			self.P1 = tk.Label(self.root2, text = self.lines[0], font=("Ariel", 16))
			self.P1.grid(row = 2, column = 0, columnspan = 2)

			self.P2 = tk.Label(self.root2, text = self.lines[1], font=("Ariel", 16))
			self.P2.grid(row = 4, column = 0, columnspan = 2)

			self.P3 = tk.Label(self.root2, text = self.lines[2], font=("Ariel", 16))
			self.P3.grid(row = 6, column = 0, columnspan = 2)

			self.P4 = tk.Label(self.root2, text = self.lines[3], font=("Ariel", 16))
			self.P4.grid(row = 8, column = 0, columnspan = 2)

			self.P1hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P1hw.grid(row = 3, column = 0)

			self.P2hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P2hw.grid(row = 5, column = 0)

			self.P3hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P3hw.grid(row = 7, column = 0)

			self.P4hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P4hw.grid(row = 9, column = 0)

			self.ent1 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent1.grid(row = 3, column = 1)

			self.ent1 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent1.grid(row = 5, column = 1)

			self.ent1 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent1.grid(row = 7, column = 1)

			self.ent1 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent1.grid(row = 9, column = 1)


			self.d2 = tk.Label(self.root2, text = "Day 2", font =("Ariel", 18))
			self.d2.grid(row = 1, column = 2, columnspan = 2)

			self.P5 = tk.Label(self.root2, text = self.lines[4], font=("Ariel", 16))
			self.P5.grid(row = 2, column = 2, columnspan = 2)

			self.P6 = tk.Label(self.root2, text = self.lines[5], font=("Ariel", 16))
			self.P6.grid(row = 4, column = 2, columnspan = 2)

			self.P7 = tk.Label(self.root2, text = self.lines[6], font=("Ariel", 16))
			self.P7.grid(row = 6, column = 2, columnspan = 2)

			self.P8 = tk.Label(self.root2, text = self.lines[7], font=("Ariel", 16))
			self.P8.grid(row = 8, column = 2, columnspan = 2)

			self.p1hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.p1hw.grid(row = 3, column = 2)

			self.p2hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.p2hw.grid(row = 5, column = 2)

			self.p3hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.p3hw.grid(row = 7, column = 2)

			self.p4hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.p4hw.grid(row = 9, column = 2)

			self.ent2 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent2.grid(row = 3, column = 3)

			self.ent2 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent2.grid(row = 5, column = 3)

			self.ent2 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent2.grid(row = 7, column = 3)

			self.ent2 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent2.grid(row = 9, column = 3)


			self.d3 = tk.Label(self.root2, text = "Day 3", font =("Ariel", 18))
			self.d3.grid(row = 1, column = 4, columnspan = 2)

			self.P9 = tk.Label(self.root2, text = self.lines[8], font=("Ariel", 16))
			self.P9.grid(row = 2, column = 4, columnspan = 2)

			self.P10 = tk.Label(self.root2, text = self.lines[9], font=("Ariel", 16))
			self.P10.grid(row = 4, column = 4, columnspan = 2)

			self.P11 = tk.Label(self.root2, text = self.lines[10], font=("Ariel", 16))
			self.P11.grid(row = 6, column = 4, columnspan = 2)

			self.P12 = tk.Label(self.root2, text = self.lines[11], font=("Ariel", 16))
			self.P12.grid(row = 8, column = 4, columnspan = 2)

			self.P1hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P1hw.grid(row = 3, column = 4)

			self.P2hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P2hw.grid(row = 5, column = 4)

			self.P3hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P3hw.grid(row = 7, column = 4)

			self.P4hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P4hw.grid(row = 9, column = 4)

			self.ent3 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent3.grid(row = 3, column = 5)

			self.ent3 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent3.grid(row = 5, column = 5)

			self.ent3 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent3.grid(row = 7, column = 5)

			self.ent3 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent3.grid(row = 9, column = 5)


			self.d4 = tk.Label(self.root2, text = "Day 4", font =("Ariel", 18))
			self.d4.grid(row = 1, column = 6, columnspan = 2)

			self.P13 = tk.Label(self.root2, text = self.lines[12], font=("Ariel", 16))
			self.P13.grid(row = 2, column = 6, columnspan = 2)

			self.P14 = tk.Label(self.root2, text = self.lines[13], font=("Ariel", 16))
			self.P14.grid(row = 4, column = 6, columnspan = 2)

			self.P15 = tk.Label(self.root2, text = self.lines[14], font=("Ariel", 16))
			self.P15.grid(row = 6, column = 6, columnspan = 2)

			self.P16 = tk.Label(self.root2, text = self.lines[15], font=("Ariel", 16))
			self.P16.grid(row = 8, column = 6, columnspan = 2)

			self.P1hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P1hw.grid(row = 3, column = 6)

			self.P2hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P2hw.grid(row = 5, column = 6)

			self.P3hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P3hw.grid(row = 7, column = 6)

			self.P4hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P4hw.grid(row = 9, column = 6)

			self.ent4 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent4.grid(row = 3, column = 7)

			self.ent4 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent4.grid(row = 5, column = 7)

			self.ent4 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent4.grid(row = 7, column = 7)

			self.ent4 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent4.grid(row = 9, column = 7)


			self.d5 = tk.Label(self.root2, text = "Day 5", font =("Ariel", 18))
			self.d5.grid(row = 10, column = 0, columnspan = 2)

			self.P17 = tk.Label(self.root2, text = self.lines[16], font=("Ariel", 16))
			self.P17.grid(row = 11, column = 0, columnspan = 2)

			self.P18 = tk.Label(self.root2, text = self.lines[17], font=("Ariel", 16))
			self.P18.grid(row = 13, column = 0, columnspan = 2)

			self.P19 = tk.Label(self.root2, text = self.lines[18], font=("Ariel", 16))
			self.P19.grid(row = 15, column = 0, columnspan = 2)

			self.P20 = tk.Label(self.root2, text = self.lines[19], font=("Ariel", 16))
			self.P20.grid(row = 17, column = 0, columnspan = 2)

			self.P1hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P1hw.grid(row = 12, column = 0)

			self.P2hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P2hw.grid(row = 14, column = 0)

			self.P3hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P3hw.grid(row = 16, column = 0)

			self.P4hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P4hw.grid(row = 18, column = 0)

			self.ent5 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent5.grid(row = 12, column = 1)

			self.ent5 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent5.grid(row = 14, column = 1)

			self.ent5 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent5.grid(row = 16, column = 1)

			self.ent5 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent5.grid(row = 18, column = 1)


			self.d6 = tk.Label(self.root2, text = "Day 6", font =("Ariel", 18))
			self.d6.grid(row = 10, column = 2, columnspan = 2)

			self.P21 = tk.Label(self.root2, text = self.lines[20], font=("Ariel", 16))
			self.P21.grid(row = 11, column = 2, columnspan = 2)

			self.P22 = tk.Label(self.root2, text = self.lines[21], font=("Ariel", 16))
			self.P22.grid(row = 13, column = 2, columnspan = 2)

			self.P23 = tk.Label(self.root2, text = self.lines[22], font=("Ariel", 16))
			self.P23.grid(row = 15, column = 2, columnspan = 2)

			self.P24 = tk.Label(self.root2, text = self.lines[23], font=("Ariel", 16))
			self.P24.grid(row = 17, column = 2, columnspan = 2)

			self.P1hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P1hw.grid(row = 12, column = 2)

			self.P2hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P2hw.grid(row = 14, column = 2)

			self.P3hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P3hw.grid(row = 16, column = 2)

			self.P4hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P4hw.grid(row = 18, column = 2)

			self.ent6 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent6.grid(row = 12, column = 3)

			self.ent6 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent6.grid(row = 14, column = 3)

			self.ent6 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent6.grid(row = 16, column = 3)

			self.ent6 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent6.grid(row = 18, column = 3)


			self.d7 = tk.Label(self.root2, text = "Day 7", font =("Ariel", 18))
			self.d7.grid(row = 10, column = 4, columnspan = 2)

			self.P25 = tk.Label(self.root2, text = self.lines[24], font=("Ariel", 16))
			self.P25.grid(row = 11, column = 4, columnspan = 2)

			self.P26 = tk.Label(self.root2, text = self.lines[25], font=("Ariel", 16))
			self.P26.grid(row = 13, column = 4, columnspan = 2)

			self.P27 = tk.Label(self.root2, text = self.lines[26], font=("Ariel", 16))
			self.P27.grid(row = 15, column = 4, columnspan = 2)

			self.P28 = tk.Label(self.root2, text = self.lines[27], font=("Ariel", 16))
			self.P28.grid(row = 17, column = 4, columnspan = 2)

			self.P1hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P1hw.grid(row = 12, column = 4)

			self.P2hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P2hw.grid(row = 14, column = 4)

			self.P3hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P3hw.grid(row = 16, column = 4)

			self.P4hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P4hw.grid(row = 18, column = 4)

			self.ent7 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent7.grid(row = 12, column = 5)

			self.ent7 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent7.grid(row = 14, column = 5)

			self.ent7 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent7.grid(row = 16, column = 5)

			self.ent7 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent7.grid(row = 18, column = 5)


			self.d8 = tk.Label(self.root2, text = "Day 8", font =("Ariel", 18))
			self.d8.grid(row = 10, column = 6, columnspan = 2)

			self.P21 = tk.Label(self.root2, text = self.lines[28], font=("Ariel", 16))
			self.P21.grid(row = 11, column = 6, columnspan = 2)

			self.P22 = tk.Label(self.root2, text = self.lines[29], font=("Ariel", 16))
			self.P22.grid(row = 13, column = 6, columnspan = 2)

			self.P23 = tk.Label(self.root2, text = self.lines[30], font=("Ariel", 16))
			self.P23.grid(row = 15, column = 6, columnspan = 2)

			self.P24 = tk.Label(self.root2, text = self.lines[31], font=("Ariel", 16))
			self.P16.grid(row = 17, column = 6, columnspan = 2)

			self.P1hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P1hw.grid(row = 12, column = 6)

			self.P2hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P2hw.grid(row = 14, column = 6)

			self.P3hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P3hw.grid(row = 16, column = 6)

			self.P4hw = tk.Label(self.root2, text = "HW: ", font=("Ariel", 16))
			self.P4hw.grid(row = 18, column = 6)

			self.ent8 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent8.grid(row = 12, column = 7)

			self.ent8 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent8.grid(row = 14, column = 7)

			self.ent8 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent8.grid(row = 16, column = 7)

			self.ent8 = tk.Entry(self.root2, bg = "#FFFFFF")
			self.ent8.grid(row = 18, column = 7)

			
		self.dataday = []

		print("Switching to daily view")
		# destroys login screen window
		if 'root3' in globals():
			root3.destroy()

		self.options = [
			"1"
			"2"
			"3"
			"4"
			"5"
			"6"
			"7"
			"8"
		]
		# Daily view is created
		self.root = tk.Tk()

		self.titleLabel = tk.Label(self.root, text = "Day", font=("Ariel", 16))
		self.titleLabel.grid(row = 0, column = 0, columnspan = 12)
		# Creating drop down menu
		self.variable = StringVar(self.root)
		self.variable.set("1")
		self.variable.trace("w", self.change)
		self.w = OptionMenu(self.root, self.variable, "1", "2", "3", "4", "5", "6", "7", "8")
		self.w.grid(row = 0, column = 7)

		self.btnGo = tk.Button(self.root, text = "Weekly", font=("Ariel", 9), command = weekview, bg = "#FFF9E8")
		self.btnGo.grid(row = 0, column = 0)
		# Reads from text file to figure out what to put in the widget
		self.P1 = tk.Label(self.root, text = self.lines[1], font=("Ariel", 16))
		self.P1.grid(row = 1, column = 0, columnspan = 12)

		self.P2 = tk.Label(self.root, text = self.lines[2], font=("Ariel", 16))
		self.P2.grid(row = 3, column = 0, columnspan = 12)

		self.P3 = tk.Label(self.root, text = self.lines[3], font=("Ariel", 16))
		self.P3.grid(row = 5, column = 0, columnspan = 12)

		self.P4 = tk.Label(self.root, text = self.lines[4], font=("Ariel", 16))
		self.P4.grid(row = 7, column = 0, columnspan = 12)

		self.P1hw = tk.Label(self.root, text = "HW: ", font=("Ariel", 16))
		self.P1hw.grid(row = 2, column = 0)

		self.P2hw = tk.Label(self.root, text = "HW: ", font=("Ariel", 16))
		self.P2hw.grid(row = 4, column = 0)

		self.P3hw = tk.Label(self.root, text = "HW: ", font=("Ariel", 16))
		self.P3hw.grid(row = 6, column = 0)

		self.P4hw = tk.Label(self.root, text = "HW: ", font=("Ariel", 16))
		self.P4hw.grid(row = 8, column = 0)

		self.ent1 = tk.Entry(self.root, bg = "#FFFFFF")
		self.ent1.grid(row = 2, column = 1, columnspan = 11)

		self.ent1 = tk.Entry(self.root, bg = "#FFFFFF")
		self.ent1.grid(row = 4, column = 1, columnspan = 11)

		self.ent1 = tk.Entry(self.root, bg = "#FFFFFF")
		self.ent1.grid(row = 6, column = 1, columnspan = 11)

		self.ent1 = tk.Entry(self.root, bg = "#FFFFFF")
		self.ent1.grid(row = 8, column = 1, columnspan = 11)

		self.root.mainloop()
	# Function that occurs every time there is a change in what is selected for the drop down menu
	def change(self, *args):
		# Creates variables that will be used to figure out what class you have
		self.i = int(self.variable.get())
		# This is a formula that figures out the index of the line of the p1 is (the day -1)*4
		self.start = (self.i - 1)*4
		# Removes previous widgets that will be replaced
		self.P1.grid_forget()
		self.P2.grid_forget()
		self.P3.grid_forget()
		self.P4.grid_forget()
		# Formula along with reading from the text files is used to consistently figure out which line to read from
		self.P1 = tk.Label(self.root, text = self.lines[self.start], font=("Ariel", 16))
		self.P1.grid(row = 1, column = 0, columnspan = 12)

		self.P2 = tk.Label(self.root, text = self.lines[self.start + 1], font=("Ariel", 16))
		self.P2.grid(row = 3, column = 0, columnspan = 12)

		self.P3 = tk.Label(self.root, text = self.lines[self.start + 2], font=("Ariel", 16))
		self.P3.grid(row = 5, column = 0, columnspan = 12)

		self.P4 = tk.Label(self.root, text = self.lines[self.start + 3], font=("Ariel", 16))
		self.P4.grid(row = 7, column = 0, columnspan = 12)										
# This function is used to send the program back to the beginning of the class
def createDayView():
	dview = Dayview() #This will create an instances of the class. 
# Login screen
root3 = Tk()
# Inserting image
img = ImageTk.PhotoImage(PIL.Image.open("UCC.png"))
panel = Label(root3, image = img)
panel.grid(row = 1, column = 0, columnspan = 2)

titleLabel = tk.Label(root3, text = "Schedule Maker", font=("Ariel", 16))
titleLabel.grid(row = 0, column = 0, columnspan = 2)

word1Label = tk.Label(root3, text = "Student ID", font=("Ariel", 10), bg = "#FFFFFF")
word1Label.grid(row = 2, column = 0, sticky = "NESW")

ent1 = tk.Entry(root3, bg = "#FFFFFF")
ent1.grid(row = 2, column = 1)

word2 = tk.Label(root3, text = " ")
# Button is connected to function createDayview which sends the code to the beginning of the class dayview
btn1 = tk.Button(root3, text = "Login", font=("Ariel", 16), command = createDayView, bg = "#FFF9E8")
btn1.grid(row = 3, column = 0, columnspan = 2, sticky = "NESW")

root3.mainloop() 