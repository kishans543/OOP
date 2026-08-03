import random

computer = random.choice([1,0,-1])
userinput = input("enter your choice:   ")
userdict = {"s":1,"w":0,"g":-1}
maindict = {1:"snack",0:"water",-1:"gun"}



if userinput not in userdict:
    print("Invalid input! Please enter s, w, or g.")
else:
    you = userdict[userinput]
    print(f"you choose {maindict[you]}, and the computer choose {maindict[computer]}")
    if(you == computer):
        print("its a draw")
    else:
        if(you == 1 and computer == 0):
            print("you win")

        elif(computer == 1 and you == 0):
            print("computer win")

        elif(you==1 and computer == -1):
            print("computer wins")
        elif(you==-1 and computer==1):
            print("you win")
        elif(you == 0 and computer == -1):
            print("you wins")
        elif(computer == 0 and you ==-1):
            print("computer wins")
        else:
            print("invalid input")   


                    



