import random


user_point = 0
computer_point = 0

exit = False

while exit == False:
    option =["rock", "paper", "scisssor"]
    user_input = input("choose rock, paper, scissor or exit: ")
    computer_input = random.choice(option)

    if user_input == "exit" :
        print("Program ended")
        print("your score is: "+ str(user_point)+ " and computer score is: "+str(computer_point))
        exit == True

    elif user_input == "rock":
        if computer_input == "rock":
            print("your input is rock ")
            print("computer input is rock ")
            print("its a tie! ")
        elif computer_input == "scissor":
            print("your input is rock")
            print("computer input is scissor")
            print("you win")
            user_point += 1
        elif computer_input == "paper":
            print("your input is rock")
            print("computer input is paper")
            print("computer win ")
            computer_point += 1


    elif user_input == "paper":
        if computer_input == "rock":
            print("your input is paper ")
            print("computer input is rock ")
            print("you win")
            user_point += 1
        elif computer_input == "scissor":
            print("your input is paper")
            print("computer input is scissor")
            print("computer win")
            computer_point += 1
        elif computer_input == "paper":
            print("your input is paper")
            print("computer input is paper")
            print("its a tie! ")


    elif user_input == "scissor":
        if computer_input == "rock":
            print("your input is scissor ")
            print("computer input is rock ")
            print("computer win ")
            computer_point += 1
        elif computer_input == "scissor":
            print("your input is scissor")
            print("computer input is scissor")
            print("its a tie! ")
            
        elif computer_input == "paper":
            print("your input is scissor ")
            print("computer input is paper")
            print("you win ")
            user_point += 1
    
    elif user_input != "rock" or user_input != "paper" or user_input != "scissor" or user_input != "exit":
        print("invalid input")
        print("enter valid input ")
