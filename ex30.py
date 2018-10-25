# Lines 1 through 3 asssigns a variable to specific numbers
people = 30
cars = 40
trucks = 15

# Lines 7, 17, and 24, has an "if" statement along with an "or" statement, that decides whether it should print the following statement or not.
if cars > people or trucks < cars:
    print("We should take the cars.")
# "Elif" is else if statement in python. It apllies in line 10, and 19.
elif cars < people:
    print("We should not take the cars.")

# Lines 14, 21, and 26, goes to an else statement only if the conditions above isn't true.
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")
