import random
'''
1 for snake
-1 for water
0 for gun
'''
computer = random.choice([-1, 0, 1])
youstr = input("Enter your choice: ")
youDict = {"s": 1, "w": -1, "g": 0}
you = youDict[youstr]
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}
print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer==you):
        print("DRAW!")
else:
        if((computer-you)==-1 or (computer-you)==2):
                print("You Lose!")
        else:
                print("You WIN!")