print("welcome to rock, paper & scicssor game")

print("Enter choice to play")
print("0 -> rock")
print("1 -> paper")
print("2 -> sicssors")

user = int(input())

import random

comp = random.randrange(3)

if user == 0:
    if comp == 0:
        print("draw")
    elif comp ==1:
        print("comp wins !!!")
    elif  comp ==2:
        print("user wins !!!")
elif comp ==1 :
    if comp == 0:
        print("user wins!!!")
    elif comp == 1 :
        print("draw")
    elif comp ==2:
        print("comp wins!!!")
elif user ==2:
    if comp ==0:
        print("comp wins!!!")
    elif comp ==1:
        print("user wins!!!")
    elif comp ==2:
        print("draw")


else:
    print("invalid input")

    print("user :", user)
    print("comp :", comp)