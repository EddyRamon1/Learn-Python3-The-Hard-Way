#It imports an argument value so when I try to execute it, It will ask for an extra input that meets the arguments
from sys import argv

#This is the types of argument values that are required to be inputted
script, filename = argv

#It will open the specific file based on what is being inputted
txt = open(filename)

#It will print out a statement along with the filename I'm trying to open
print(f"Here's your file {filename}:")

#It prints out the filename and what's inside the file (In this case ex15_sample.txt)
print(txt.read())

#It asks to type the filename again
print("Type the filename again:")

#It asks the user to input the filename so the program will execute again. 
file_again = input("> ")

#It opens the file again 
txt_again = open(file_again)

#prints out what's in the file again
print(txt_again.read)
