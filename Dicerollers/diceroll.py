#Tabletop Diceroller
import random
from random import choice, randint

rolls = []
#Roll D4
def d4 ():
    return random(0,4)

#Roll D6
def d6 ():
    return random(0,6)

#Roll D8
def d8 ():
    return random(0,8)

#Roll D10
def d10 ():
    return random(0,10)

#Roll D12
def d12 ():
    return random(0,12)

#Roll D20
def d20 ():
    return random.randint(0,20)


print("Select Dice")
print("1 - D4")
print("2 - D6")
print("3 - D8")
print("4 - D10")
print("5 - D12")
print("6 - D20")

#Get user input
while True:
    choice = input ("Enter Choice(1, 2, 3, 4, 5, 6): ")

#Make sure input was valid
    if choice == '1':
        print(d4)

    elif choice == '2':
        print(d6)
    
    elif choice == '3':
        print(d8)

    elif choice == '4':
        print(d10)
    
    elif choice == '5':
        print(d12)
    
    elif choice == '6':
        print(d20)
    
    else:
        print("Invalid option")