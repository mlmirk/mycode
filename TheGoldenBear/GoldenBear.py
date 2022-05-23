#!/usr/bin/python3
import os

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
    #print a main menu and the commands
    print('''
RPRG Game (Second R is for riddle!)
========
Commands:
    go [direction]
    get [item]
    combine[inventory]
    offer[your creation]

''')

def showStatus():
    #print the player's current status
    print('---------------------------')
    print('You are in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "items" in rooms[currentRoom]:
        for x in rooms[currentRoom]['items']:
            print("You see" ,x)
    if "message" in rooms[currentRoom] and rooms[currentRoom]['message'].__len__() >1:
        print(rooms[currentRoom]['message'][lives])
    elif "message" in rooms[currentRoom] :
        print(rooms[currentRoom]['message'][0])
        #print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

#an inventory, which is initially empty
inventory = []
lives=2
drink=''
#a dictionary linking a room to other rooms
## A dictionary linking a room to other rooms
rooms = {

            'Den' : {
                    'south' : 'Kitchen',
                    'message': ["he flips you the BIRDIE get me my drink, last chance",
                    "He raises a CLUB towards you this is wrong try again",
                    "A golden bear sits before you in the den. It speaks to you 'I require MY bevarage fill up my glass and you shall be able to leave!'"]
                },

            'Kitchen' : {
                    'north' : 'Den',
                    'east':'Icebox',
                    'west':'Cupboard',
                    'south' : 'Counter'
                    ,
                    'message'  : ['You stand in a Vast kitchen a space s large you are confused why you walk to far before seeing whays on each wall'],
                },
            'Icebox' : {
                    'west' : 'Kitchen',
                    'items' : ['tea','pepsi','whiskey','milk',
                    'chocolate sryup','yohoo','orange juice','lemonade',
                    'vodka','champagne','ice', 'beer']
                    
                },
            'Cupboard' : {
                    'east' : 'Kitchen',
                    'items':['pint-glass', 'shot-glass', 'das-boot', 'tea-cup']
                },
            'Counter' : {
                    'north' : 'Kitchen',
                    'message' : ['careful if you chose to create the drink all items will be taken and combined to create a drink']
            }
            }

#start the player in the Den
currentRoom = 'Den'

showInstructions()

#loop forever
while True:
    showStatus()

    #get the player's next 'move'
    #.split() breaks it up into an list array
    #eg typing 'go east' would give the list:
    #['go','east']
    move = ''
    while move == '':
        move = input('>')
    # split allows an items to have a space on them
    # get golden key is returned ["get", "golden key"]          
    move = move.lower().split(" ", 1)

    #if they type 'go' first
    if move[0] == 'go' and move.__len__()>1 : 
        #check that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
        #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' and move.__len__()>1 :
        print(rooms[currentRoom]['items'])
            #if the room contains an item, and the item is the one they want to get
        if "items" in rooms[currentRoom] and move[1] in rooms[currentRoom]['items']:
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' got!')
            #delete the item from the room
            temp = rooms[currentRoom]['items']
            remove= temp.index(move[1])
            del rooms[currentRoom]['items'][remove]
            #print(rooms[currentRoom]['items'])
#otherwise, if the item isn't there to get
        else:
#tell them they can't get it
            print('Can\'t get ' + move[1] + '!')


    if move[0] == 'combine' and currentRoom == 'Counter':
        print("hitting")
        if "lemonade" and "tea" and "ice" and 'pint-glass' in inventory:
            inventory.clear()
            inventory.append('arnold palmer')
        elif "champagne" and "orange juice" and 'pint-glass' in inventory:
            inventory.clear()
            inventory.append('mimosa')
        elif "vodka" and "orange juice" and 'pint-glass' in inventory:
            inventory.clear()
            inventory.append('screwdriver')
        elif "milk" and "pepsi" and ("pint-glass" or "shot-glass" or 'das-boot'or 'tea-cup'):
            inventory.clear()
            inventory.append('pilk')
        elif "milk" and "chocalate syrup" and ("pint-glass" or "shot-glass" or 'das-boot'or 'tea-cup') in inventory:
            inventory.clear()
            inventory.append('chocolate milk')
        elif "beer"  and 'das-boot' in inventory:
            inventory.clear()
            inventory.append('DAS BOOT OF FINE GERMAN BEER')
        elif "whiskey" and 'yohoo'  and ("pint-glass" or "shot-glass" or 'das-boot'or 'tea-cup')in inventory:
            inventory.clear()
            inventory.append('A Lou Stratia Specialy Brought to you from Bayonne, NJ')
        else:
            inventory.append('an elixer of beverage')

    if move[0] =='offer' and currentRoom == 'Den':
        if 'arnold palmer' in inventory:
            print("Congrats Arnold Palmer just wanted an Arnold palmer good job, you may leave")
            break
        elif 'pilk' in inventory:
            print("It matters not how much pilk is consumer a single drop of pilk is enough to kill\n Congrats You have killed Arnold Palmer")
            break
        elif lives > 0:
            lives-=1
            print("Try and create another Bev")
        else:
            print("The Golden Bear takes a nine iron to you and you have died")
            break
    os.system('clear')   
    if move[0] == 'combine' and rooms[currentRoom] != 'Counter':
        print("You must be at the counter to do this")

    if move[0] == 'offer' and currentRoom != 'Den':
        "You can only offer the Golden Bear the drink in the den"
    
