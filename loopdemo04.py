# loop can repeat a section of code.
# It can run the same code over and over or
# generate a pattern.

# Conditional loops: Go as long as a condition is true

# Counted loops: These loops use a counter to keep
#				 Track of how many times the loop has run
# If you know how many times a loop should run it's beter to use counter loop
# Else use conditional loop
import os
print("*******************************")
#Taking inputs
word = input("Please input a word with more than 5 letters ")
#print(word.isalpha())
while (len(word) < 6 or word.isalpha() == False):
	word = input("Please input a word with more than 5 letters ")
	if (len(word) < 6):
		print("Boi learn to count letters that's not enough")
		os.system("say mission failed we will get them next time")

	if (word.isalpha() == False):
		print("boi use one word")


print(word+" is seriously long!")