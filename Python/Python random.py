import random

suffix = "st"

for i in range(0,5,1):

    print("______________________________________________________________________________\n")
    
    rand = random.randint(0,9)
    your_guess = input("Guess the number! \n enter the number and see your luck! \n number: ")

    rand = str(rand)
    your_guess = str(your_guess)

    if(i+1 == 1):
        suffix = "st"
    elif(i+1 == 2):
        suffix = "nd"
    elif(i+1 == 3):
        suffix = "rd"
    else:
        suffix = "th"
    
    print ("\nThe number is... " + rand + "!!! \n")

    if(rand == your_guess):
        print("\nLooks like you won!!\n")
        break
    else:
        if(i != 4):
            print("\nWanna try your luck again?\n")
            print("This was your " + str(i+1) + suffix + " try\n you have " + str(5-(i+1)) + " tries left\n")
        else:
            print("\nLooks like you lost\n")
