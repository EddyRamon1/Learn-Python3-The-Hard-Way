# I prefer this verion of the game and I don't want to change it.
print(""" You enter a dark room with two doors.print
Do you go through Door #1, Door #2?""")

Door = input("> ")

if Door == "1":
    print("There's a giant bear here eating a cheese cake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    Bear = input("> ")
    
    if Bear == "1":
        print("The bear eats your face off. Good job!")
    elif Bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well doing {Bear} is probably better.")
        print("Bear runs away.")

elif Door == "2":
    print("You stare into the endless abyss at Cthulhu's retina.")
    print("What will you choose?")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understanding revolvers yelling melodies.")

    Insanity = input("> ")

    if Insanity == "1" or Insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes into a pool of muck.")
        print("Good job!")

else:
    print("You stumble around and fall on a knife and die. Good job!")
