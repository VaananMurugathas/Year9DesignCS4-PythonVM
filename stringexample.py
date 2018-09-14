#This file will go through the basics of string manipulation

name = input("What is your name: ")
print(name)
sentence = name + " is cool" #concatination is adding terms
print(sentence)

#Access specific letters
fletter = name[0]
print(fletter)
letters1 = name[0:2]
print(letters1)
for i in range(len(name)):
	print(name[i])