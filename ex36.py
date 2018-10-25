from sys import exit

def gold_room():
    print("You reached a sanctuary. How many years would you like to spend in?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 60:
        print("It seems you got tired of this place overtime. You Win!")
        exit(0)
    else:
        dead("Looks like the next adventurers found your dead body.")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input("> ")
        
        if choice == "take honey":
            dead("The bear looks at you then cries. Nice going jerk")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and ripped your eyes out. That's gotta hurt")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("Yes I'm sorry I do not speak English, ok.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or play Super Smash Bros.?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "play" in choice:
        dead("You've wasted more than 5 years of playing Super Smash Bros. and died becasuse you now realized you didn't eat for 5 years.")
    else:
        cthulhu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input("> ")
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
        
        
start()
