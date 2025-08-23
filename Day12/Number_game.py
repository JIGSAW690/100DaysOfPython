from art import logo
import random
print(logo)

attempt = 0
game_on = True
game_num = random.randint(1,101)

def easy_or_hard():
    global attempt
    global game_num
    choice = input("Welcome to the Number Guessing Game\nI'm thinking of a number between 1 and 100\nChoose a difficulty. Type 'easy' or 'hard'").lower()
    if(choice=='easy'):
        attempt = 10
        print("you have 10 attempts remaining to guess the number")
    elif(choice=='hard'):
        attempt = 5
        print("you have 5 attempts remaining to guess the number")
    else:
        print("Invalid Input, choose either 'easy' or 'hard'")
        return
    for i in range(attempt):
        guess = int(input('Make a guess\n'))
        if (guess == game_num):
            print("You've guessed it correctly. You win, congrats")
            attempt = 0
            return
        elif (guess < game_num):
            if(attempt != 1):
                print("Too low.\nGuess again.")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        elif (guess > game_num):
            if (attempt != 1):
                print("Too High.\nGuess Again!")
            attempt -= 1
            print(f"You have {attempt} attempts remaining to guess the number.")
        else:
            pass

while game_on:
    easy_or_hard()
    if(attempt==0):
        print('You have utilized all your attempts, play again from starting')
        game_on = False




