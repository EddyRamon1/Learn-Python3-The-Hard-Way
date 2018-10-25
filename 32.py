the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

#Below is an example of a for-loop in Python
for number in the_count:
    print(f"This is count {number}")

#Same for-loop from above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

#It can go through mixed lists
#{} parameters is required for assigned variables
for i in change:
    print(f"I got {i}")

#It can alse build lists
elements = []

#There is also range functions to do 0 to 5 counts
for i in range(0, 6):
    print(f"Adding {i} to the list.")
    #Append is a function that lists understand
    elements.append(i)

#It can also be printed out
for i in elements:
    print(f"Element was: {i}")
