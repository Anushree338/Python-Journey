import random

computer = random.choice([-1 , 0, 1])
yourstr = input("Enter your choice: ")
youDict= {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = youDict[yourstr]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if(computer == you):
    print("It's a Draw!")

else:
    if((computer - you) == -1 or (computer - you) == 2):
        print("You lose!")
    else:
        print("You win")