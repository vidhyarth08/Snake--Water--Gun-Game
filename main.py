import random as rand
'''
1 for snake
-1 for water
0 for gun
'''
computer = rand.choice([-1,0,1])
yourChoice = input("Enter your choice: ")
yourDict = {"s": 1, "w": -1, "g": 0}
reverseDict = {1: "Snake", -1: "Water", 0: "Gun"}

you = yourDict[yourChoice]

print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

if computer == you:
    print("It's a draw!")

else:
    if computer == -1 and you == 1:
        print("You win!")

    elif computer == -1 and you == 0:
        print("You lose!")
        
    elif computer == 1 and you == -1:
        print("You lose!")

    elif computer == -1 and you == 0:
        print("You win!")        
        
    elif computer == 0 and you == -1:
        print("You win!")

    elif computer == 0 and you == 1:
        print("You lose!")      

    else:
        print("Invalid choice!\nSomething went wrong!")    

# or you can just write the below if , else statement to save time.
#if((computer - you) == -1) or (computer - you) == 2):
#   print("You lose!")
#else:
#   print("You win!")