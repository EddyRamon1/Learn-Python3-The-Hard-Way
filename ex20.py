#It's creating an argument so we can input the execution in the terminal
from sys import argv

#this is the inputs of argv to type it into the terminal
script, input_file = argv

#It defines the variable and reads an assigned file.
def print_all(f):
    print(f.read())

#It defines another variableand assigns a numbers    
def rewind(f):
    f.seek(0)

#It defines another variable and prints the functions on the text document
def print_a_line(line_count, f):
    print(line_count, f.readline())

#It opens the file of the text document
current_file = open(input_file)

#It prints the sentence and a new line
print("First let's print the whole file:\n")

#It tells to print out the text document
print_all(current_file)

#It prints ot another statement
print("Now let's rewind, kind of like a tape.")

#It redos the file reading and opening
rewind(current_file)

#It prints another statements
print("Let's print three lines:")

#It executes the documents to read the text file
current_line = 1
print_a_line(current_line, current_file)

#It executes the documents to read the text file
current_line = current_line  + 1
print_a_line(current_line, current_file)

#It executes the documents to read the text file
current_line = current_line + 1
print_a_line(current_line, current_file)
