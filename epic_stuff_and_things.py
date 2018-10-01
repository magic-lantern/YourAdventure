# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sys

print("")
print("")
print("")
print( "Epic Stuff and Things" )
print( "By: Levi Russell")
name = input("Enter your name: ")
color = input("Enter a color: ")
print("")
print("Welcome to epic stuff and things")

inv = []

troll = True

goblin = True

water_bottle = True

shatterd = False

#def iremove_inv(i):
#    if check_inv(i):
#        inv.remove(i)
#    else:
#        print("You don't seem to have", i , "in your inventory")

def remove_inv(i):
    try:
        inv.remove(i)
    except ValueError:
        print("You don't seem to have", i , "in your inventory")
        

def add_to_inv(i):
    for item in inv:
        if (i == item):
            print("You already have that in your inventory")
            return
    inv.append(i)

def show_inv():
    print(inv)
    
def check_inv(i):
    if i in inv:
        return True
    return False
    
 
def attic_room():
    cupboard = False
    print("Hello " + name + " you are up in the attic of the " + color + " house.")
    print("There is a large cupboard south of you. There are stairways leading to")
    print("the north and east.")
    
    while True:
        move = input("What would you like to do? ")
        if move == 'east':
            living_room()
        elif move == 'north':
            kitchen()
        elif move == 'inv':
            show_inv()
        elif move == 'open cupboard':
            if check_inv("bronze key"):
                print("In the cubard there is a hammer")
                cupboard = True
            else:
                print("looks like the cupboard is locked") 
        elif move == 'take hammer' and cupboard == True:
            print("got hammer")
            add_to_inv("hammer")
        elif move == 'inv':
            show_inv()
        else:
            print("I'm not sure what you mean. ")
            
def front_room():
    global troll
    if troll:
        print(name + " is now in the front room of the " + color + " house. There ")
        print("is a troll blocking your way outside.")
    else:
        print("You are now in the front room of the " + color+ " house. There is")
        print("a dead troll on the ground. There are doors to the north and west.")
    
    while True:
        move = input("what would you like to do? ")
        if move == 'west':
            kitchen()
        elif move == 'north' and troll:
            print("The troll is blocking your way.")
        elif move == 'north' and not troll:
            field()
        elif move == 'kill troll':
            if check_inv("sword"):
                troll = False
                print("Troll dies.")
            else :
                print("You don't have the object.")
        elif move == 'inv':
            show_inv()
        else:
            print("I'm not sure what you mean.")
            
def field():
    print("""You are in a field north of the house, there is a path to the east
and a door to the south.""")
    
    while True:
        move = input("What would you like to do? ")
        if move == 'south':
            front_room()
        elif move == 'east':
            forest()
        elif move == 'inv':
            show_inv()
        else:
            print("I'm not sure what you mean.")
            
def forest():
    global goblin
    if goblin:
        print("You are in a forest with a gobin blocking your way, the goblin has a ax.")
    else:
        print("You are in a forest there is a dead goblin on the ground.")
    
    while True:
        move = input("What would you like to do? ")
        if move == 'west' and goblin and check_inv("sword"):
            print("The goblin blockes your way.")
        elif move == 'west' and not goblin:
            field()
        elif move == 'kill goblin':
            if check_inv("sword"):
                goblin = False
                print("The goblin is dead.")
        elif move == 'take ax' and goblin:
            print("The goblin has the ax and will not give it to you.")
        elif move == 'take ax' and not goblin:
            print("got ax")
            add_to_inv("ax")
        elif move == 'inv':
            show_inv()
        else:
            print("I'm not sure what you mean. ")
            
            
def living_room():
    timeslook = 0
    couch = 0
    print("""You are now in the living room there is a large couch blocking 
the door to the east""")
    
    while True:
        move = input("What would you like to do? ")
        if move == 'west':
            attic_room()
        elif move == 'east':
            grove()
        elif move == 'open door':
            print("The door is blocked")
        elif move == 'look in couch':
            if timeslook == 0:
                print("Found sword") 
                add_to_inv("sword")
                timeslook += 1
            elif timeslook == 1:
                print("Found bronze key")
                add_to_inv("bronze key")
                timeslook += 1
            else:
                print("There is nothing left in the couch")
        elif move == 'move couch':
            couch += 1
            if couch % 2 == 1:
                print("""with a great effort you move the couch away from the door""")
            elif couch % 2 == 0:
                print("with a great effort you move the couch back.")
        elif move == 'inv':
            show_inv()
        else:
            print("I'm not sure what you mean. ")

def kitchen():
    global water_bottle
    global shatterd
    if water_bottle and not shatterd:
        print("""You are in the kitchen and there is a black water bottle on the table 
and stairs to the south of you and a door to the east""")
    elif not water_bottle and not shatterd:
        print("""You are know in the kitchen and there is a empty table next to you. 
There is a door to the east of you and stairs leading to the south""")
    elif not water_bottle and shatterd:
        print("""You are know in the kitchen and a shatterd water bottle is all over the 
floor and a table is just sitting there. There is a door to the east and stairs to 
the south""")

    while True:
        move = input("What would you like to do? ")
        if move == 'east':
            front_room()
        elif move == 'south':
            attic_room()
        elif move == 'take black water bottle':
            print("Got black water bottle and you heard a jingle.")
            add_to_inv("black water bottle")
            water_bottle = False
        elif move == 'throw water bottle' and not shatterd:
            print("The black water bottle shatters and reveals a silver key")
            shatterd = True
            add_to_inv("silver key")
            remove_inv("black water bottle")
        elif move == 'throw water bottle' and shatterd:
            print("You don't have a water bottle.")
        elif move == 'inv':
            show_inv()
        elif move == 'test':
            remove_inv("black water bottle")
        else:
            print("I'n not sure what you mean.")

def grove():
    print("""You are now outside in a grove of trees""")
    sys.exit()
    
attic_room()