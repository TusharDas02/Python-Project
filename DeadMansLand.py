print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
''')
print("Welcome to the Dead Man's Land.")
print("Your mission is to find the treasure or escape the place, but be careful of the monster lurking around.")

has_torch = False
has_key = False

direction = input("You are at a cross road, where do you want to go? Type 'left' or 'right' \n").lower()

if direction == "right":
    print("\nThe fog thickens....you can't breathe...you are dead.")
elif direction == "left":
    print("\nYou enter a dark forest and hear something behind you")
    choice = input("Do you want to run or stay? Type 'run' or 'hide' \n").lower()
    if choice == "run":
        print("\nYou run as fast as you can but you can't escape the monster and you are dead.")    
    elif choice == "hide":
        print("\nYou hide behind a tree and the monster passes by you and you are safe for now.")
        item = input("You see a torch and a key on the ground, which one do you want to pick up? Type 'torch' or 'key' \n").lower() 
        if item == "torch":
            has_torch = True    
        elif item == "key":
            has_key = True
        print("\nYou continue walking and find a mysterious door, you need a key to open it.")
        choice = input("Do you want to open the door? or escape the place? Type 'open' or 'escape' \n").lower()
        if choice == "open":
            if has_key:
                print("\nYou use the key to open the door and find the treasure, you win!")
            else:
                print("\nYou don't have the key and the trap activates and squashes you, you are dead.")
        elif choice == "escape":
            if has_torch:
                print("\nYou use the torch to light your way and escape the place, you win!")
            else:
                print("\nYou try to escape but you can't see anything and something in the darkness finds you and you are dead.")
        else:
            print("\nYou can't decide and the monster finds you and you are dead.")
    
    else:
        print("\nYou freeze in fear and the monster finds you and you are dead.")

input("Enter to exit the game.")