#Create by Justin Lo 
#import
import os
#Run terminal
os.system("cd desktop")
os.system("cd Programming")
os.system("cd Year9DesignCS4-PythonVM")
#Take comment
text=input('What is your comment for commit: ')

os.system("git status")
os.system("git add .")

sentence = str('git commit -m "{0}"'.format(text))
os.system(sentence)

os.system("git push")