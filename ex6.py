# The variable "types_of_people" is assigned to the number 10
types_of_people = 10

# The variable "x" is assigned to a print statement encoded with "types_of_people" variable
x = f"There are {types_of_people} types of people."

# Variable "binary" is assigned to a printed "binary"
binary = "binary"

# Variable "do_not" is assigned to a printed "don't"
do_not = "don't"

# Variable "y" is assigned to a printed statement that plugs in the previous variables in a printed sentence.
y = f"Those who know {binary} and those who {do_not}."

# Prints the variable that was previously assigned
print(x)

# Prints the variable that was previously assigned.
print(y)

# prints out a quoted statement along with a variable encoded inside.
print(f"I said: {x}")

# prints out a quoted statement along with a variable encoded inside.
print(f"I also said: '{y}'")

# The variable "hilarious" is assigned to a false statement
hilarious = False

# The variable "joke_evaluation" is assigned to a printed statement with an empty open-closed curly braces.
joke_evaluation = "Isn't that joke so funny?! {}"

# It prints out a format which prints out the previous assigned statement.
print(joke_evaluation.format(hilarious))

# Variable "w" is assigned to a print statement 
w = "This is the left side of..."

# Variable "e" is assigned to a print statement
e = "a string with a right side."

# It prints out both variables as a string
print(w + e)
