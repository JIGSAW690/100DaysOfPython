from art import logo
import random

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
user = []
computer = []
game_on = True
sum_user = 0
sum_computer = 0
count_user = 0
count_computer = 0
sum_u = 0
comp_u = 0


for i in range(2):
    user.append(random.choice(cards))
    computer.append(random.choice(cards))

def blackjack(sum_user, sum_computer, count_user, count_computer, sum_u):
    global game_on
    sum_user = 0
    sum_computer = 0
    count_user = 0
    count_computer = 0
    sum_u = 0
    comp_u = 0
    for elements in user:
        sum_user += elements
    for elements in computer:
        sum_computer += elements
    if ((10 in user) and (11 in user)):
            count_user += 1
    if ((10 in computer) and (11 in computer)):
            count_computer += 1
    if(count_user == 1):
        print('User has a BlackJack, User Wins')
        game_on = False
        return
    if(count_computer == 1):
        print('Computer has a BlackJack, Computer Wins')
        game_on = False
        return
    if(sum_user>21):
        if 11 not in user:
            print('Computer Wins')
            game_on = False
            return
        else:
            for elements in user:
                if elements == 11:
                    sum_u += 1
                else:
                    sum_u += elements
            if(sum_u>21):
                print('Computer Wins')
                game_on = False
                return
            else:
                choice = input('Do you want to draw another card from the deck?\n').lower()
                if choice == 'no':
                    if(sum_computer<17):
                        game_on = True
                    if(sum_computer>21):
                        print('You Win')
                        game_on = False
                        return
                    else:
                        if(sum_user==sum_computer):
                            print('Draw')
                        elif(sum_computer>sum_user):
                            print('Computer Wins')
                        else:
                            print('You Win')
                        game_on = False
                        return
                else:
                    user.append(random.choice(cards))
                    computer.append(random.choice(cards))
                    blackjack(sum_user, sum_computer, count_user, count_computer, sum_u)

    elif (sum_computer > 21):
        if 11 not in computer:
            print('You Win')
            game_on = False
            return
        else:
            for elements in computer:
                if elements == 11:
                    comp_u += 1
                else:
                    comp_u += elements
            if (comp_u > 21):
                print('You Win')
                game_on = False
                return
    else:
        choice1 = input('Do you want to draw another card from the deck?\n').lower()
        if choice1 == 'no':
            if (sum_computer < 17):
                game_on = True
            if (sum_computer > 21):
                print('You Win')
                game_on = False
                return
            else:
                if (sum_user == sum_computer):
                    print('Draw')
                    return
                elif (sum_computer > sum_user):
                    print('Computer Wins')
                    return
                else:
                    print('You Win')
                game_on = False
                return
        else:
            user.append(random.choice(cards))
            computer.append(random.choice(cards))
            blackjack(sum_user, sum_computer, count_user, count_computer, sum_u)


while game_on:
    blackjack(sum_user, sum_computer, count_user, count_computer, sum_u)

for i in range(len(user)):
    print(f"User's deck was : {user[i]}, Computer's deck was : {computer[i]}")