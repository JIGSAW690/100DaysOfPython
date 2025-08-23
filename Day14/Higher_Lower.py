import art
from game_data import data
import random

game_on = True
score = 0
a = random.choice(data)
b = random.choice(data)

def higher_lower(a,b):
    print(art.logo)
    global score
    global game_on
    print(f"Compare A: {a['name']}, a {a['description']}, from {a['country']}\n")
    print(art.vs)
    print(f"Against B: {b['name']}, a {b['description']}, from {b['country']}\n")
    choice = input("Who has more followers? Type 'A' or 'B':\t").upper()
    if (choice == 'A'):
        if (a['follower_count'] > b['follower_count']):
            score += 1
            print(f"You're right! Current Score: {score}")
            b = random.choice(data)
            higher_lower(a,b)
        else:
            print(f"Sorry that was wrong. Final Score: {score}")
            game_on = False
            return
    else:
        if (a['follower_count'] < b['follower_count']):
            score += 1
            print(f"You're right! Current Score: {score}")
            a = b
            b = random.choice(data)
            higher_lower(a,b)
        else:
            print(f"Sorry that was wrong. Final Score: {score}")
            game_on = False
            return


while game_on:
    higher_lower(a,b)



