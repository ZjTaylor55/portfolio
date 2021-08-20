#Tabletop Diceroller
import random
from random import choice, randint

#Ask for which dice needs to be rolled.
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
        print(random.randint(0,4))

    elif choice == '2':
        print(random.randint(0,6))
    
    elif choice == '3':
        print(random.randint(0,8))

    elif choice == '4':
        print(random.randint(0,10))
    
    elif choice == '5':
        print(random.randint(0,12))
    
    elif choice == '6':
        print(random.randint(0,20))
    
    else:
        print("Invalid option")