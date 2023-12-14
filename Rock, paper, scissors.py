import random as rd

# creating a rock, paper, scissors game
rock = 1
paper = 2
scissors = 3

count = 0
cpu_score = 0
user_score = 0

print("Lets have a game of rock, paper, scissors! Best out of 3 wins!")

while count < 3:

    # random integer for cpu, user enters choice
    cpu_choice = rd.randint(1,3)
    user_choice = int(input("Input 1 for rock, 2 for paper, 3 for scissors:"))

    # if-elif statement to determine match winner
    if cpu_choice == user_choice:
        print(f"Match {count + 1}:")
        print("It's a tie!\n")
        count += 1

    elif cpu_choice == 1 and user_choice == 2:
        print(f"Match {count + 1}:")
        print("Computer chose rock, user chose paper. Paper beats rock!")
        print("You win!\n")
        count += 1
        user_score +=1

    elif cpu_choice == 1 and user_choice == 3:
        print(f"Match {count + 1}:")
        print("Computer chose rock, user chose scissors. Rock beats scissors!")
        print("You lose!\n")
        count += 1
        cpu_score += 1

    elif cpu_choice == 2 and user_choice == 1:
        print(f"Match {count + 1}:")
        print("Computer chose paper, user chose rock. Paper beats rock!")
        print("You lose!\n")
        count += 1
        cpu_score += 1

    elif cpu_choice == 2 and user_choice == 3:
        print(f"Match {count + 1}:")
        print("Computer chose paper, user chose scissors. Scissors beat paper!")
        print("You win!\n")
        count += 1
        user_score +=1

    elif cpu_choice == 3 and user_choice == 1:
        print(f"Match {count + 1}:")
        print("Computer chose scissors, user chose rock. Rock beats scissors!")
        print("You win!\n")
        count += 1
        user_score +=1

    elif cpu_choice == 3 and user_choice == 2:
        print(f"Match {count + 1}:")
        print("Computer chose scissors, user chose paper. Scissors beats rock!")
        print("You lose!\n")
        count += 1
        cpu_score += 1

    else:
        print("Please only input 1, 2 or 3")

# print outcome of game
print(f"The final score is:\n Computer: {cpu_score} \n User: {user_score}")

if cpu_score == user_score:
    print("It's a tie!")

elif cpu_score > user_score:
    print("The computer wins, better luck next time!")

elif cpu_score < user_score:
    print("Well done, you have won the game!")
