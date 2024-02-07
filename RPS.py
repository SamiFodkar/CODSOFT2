import random

User_choice = int(input("Enter Your Choice :Type 0 For Rock, 1 For Paper, 2 For Scissor :"))
if User_choice >= 3 or User_choice < 0:
	print("INVALID NUMBER,YOU LOSE THE MATCH !")
else:
    Computer_choice = random.randint(0,2)
    print("Computer Chose :")
    print(Computer_choice)
    if Computer_choice == User_choice:
	    print("Match Draw..!")
    elif Computer_choice == 0 and User_choice == 2:
	    print("You Lose.!")
    elif User_choice == 2 and Computer_choice == 0:
	    print("You Win.!")
    elif Computer_choice > User_choice:
	    print("You Lose the match.!")
    elif User_choice > Computer_choice:
	    print("You Win the match.!")

    print("you want to play again ? ")
