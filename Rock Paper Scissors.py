import random
import os

rock = 0
paper = 0
scissors = 0
x = 0
rock2 = 0
paper2 = 0
scissors2 = 0
draws = 0
fails = 0
win = 0
lose = 0


while (1):

    print("Rock Paper Scissors!")
    print("")
    print("Rock(1)")
    print("Paper(2)")
    print("Scissors(3)")
    print("")

    chosen = input("> ")
    option = str(chosen)
    option = option.lower()
    


    if option == "1":
        rock += 1
        
        print("")

        genoptions = ["Rock", "Paper", "Scissors"]
        choice = random.choice(genoptions)
        print("The computer chose: " + choice)
        choice = choice.lower()
        
        ##stats
        if choice == "rock":
            rock2 +=1
        elif choice == "paper":
            paper2 +=1
        elif choice == "scissors":
            scissors2 +=1

        option = "rock"
        print("")

        if option == choice:
            print("It's a draw!")
            draws +=1

        elif option != choice:
            if option == "rock" and choice == "paper":
                print("The computer won!")
                lose +=1
            elif option == "paper" and choice == "rock":
                print("You won!")
                win +=1
            elif option == "scissors" and choice == "rock":
                print("The computer won!")
                lose +=1
            elif option == "rock" and choice == "scissors":
                print("You won!")
                win +=1
            elif option == "scissors" and choice == "paper":
                print("You won!")
                win +=1
            elif option == "paper" and choice == "scissors":
                print("The computer won!")
                lose +=1

        else:
            print("null")

    elif option == "2":
        paper += 1

        print("")

        genoptions = ["Rock", "Paper", "Scissors"]
        choice = random.choice(genoptions)
        print("The computer chose: " + choice)
        choice = choice.lower()
        
        ##stats
        if choice == "rock":
            rock2 +=1
        elif choice == "paper":
            paper2 +=1
        elif choice == "scissors":
            scissors2 += 1

        option = "paper"
        print("")

        if option == choice:
            print("It's a draw!")
            draws +=1

        elif option != choice:
            if option == "rock" and choice == "paper":
                print("The computer won!")
                lose +=1
            elif option == "paper" and choice == "rock":
                print("You won!")
                win +=1
            elif option == "scissors" and choice == "rock":
                print("The computer won!")
                lose +=1
            elif option == "rock" and choice == "scissors":
                print("You won!")
                win +=1
            elif option == "scissors" and choice == "paper":
                print("You won!")
                win +=1
            elif option == "paper" and choice == "scissors":
                print("The computer won!")
                lose +=1

        else:
            print("null")

    elif option == "3":
        scissors += 1

        print("")

        genoptions = ["Rock", "Paper", "Scissors"]
        choice = random.choice(genoptions)
        print("The computer chose: " + choice)
        choice = choice.lower()
        
        ##stats
        if choice == "rock":
            rock2 +=1
        elif choice == "paper":
            paper2 +=1
        elif choice == "scissors":
            scissors2 +=1

        option = "scissors"
        print("")

        if option == choice:
            print("It's a draw!")
            draws +=1

        elif option != choice:
            if option == "rock" and choice == "paper":
                print("The computer won!")
                lose +=1
            elif option == "paper" and choice == "rock":
                print("You won!")
                win +=1
            elif option == "scissors" and choice == "rock":
                print("The computer won!")
                lose +=1
            elif option == "rock" and choice == "scissors":
                print("You won!")
                win +=1
            elif option == "scissors" and choice == "paper":
                print("You won!")
                win +=1
            elif option == "paper" and choice == "scissors":
                print("The computer won!")
                lose +=1

        else:
            print("null")

    elif option == "stats":
        meow = x-fails
        print("")
        print("Times you chose Rock: "+str(rock))
        print("Times you chose Paper: "+str(paper))
        print("Times you chose Scissors: "+str(scissors))
        print("Times computer chose Rock: "+str(rock2))
        print("Times computer chose Paper: "+str(paper2))
        print("Times computer chose Scissors: "+str(scissors2))
        print("Times drawn: "+str(draws))
        print("Times you failed to write correctly: "+str(fails))
        print("Times you won: "+str(win))
        print("Times the computer won: "+str(lose))
        print("Times played: "+str(meow))
    
    elif option == "quit" or "exit":
        exit()

    else:
        print("Your input is invalid!")
        print("Please try again.")
        fails +=1

    input()
    x += 1
    os.system('cls')