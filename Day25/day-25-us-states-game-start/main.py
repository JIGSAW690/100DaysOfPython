import turtle
import pandas

FONT = ('Arial', 8, 'normal')
ALIGNMENT = 'center'

#Setting the screen for the game
screen = turtle.Screen()
screen.title("U.S. States Game Start")
image = 'blank_states_img.gif'
screen.addshape(image)
turtle.shape(image)

#Using pandas to retrieve data from csv file
states_data = pandas.read_csv('50_states.csv')
state_list = states_data['state'].tolist()

guess_list = []
guess = 0
total = len(state_list)
new_list = []

#Main Game Logic
game_on = True
while game_on:
    answer_state = screen.textinput(title=f'Guess the State. {guess}/{total} guessed.', prompt='What is another state?').title()
    if answer_state == "Exit":
        break
    if answer_state in state_list:
        index = state_list.index(answer_state)
        state_row = states_data[states_data['state'] == answer_state]
        turtle.penup()
        turtle.goto(float(state_row.x), float(state_row.y))
        turtle.pencolor('Black')
        turtle.write(f'{str(state_list[index])}', align=ALIGNMENT, font=FONT)
        turtle.home()
        guess += 1
        guess_list.append(answer_state)
    else:
        continue
    if guess == total:
        game_on = False

#Using List Comprehension instead of regular for loop
new_list = [state for state in state_list if state not in guess_list]

"""
for state in state_list:
    if state not in guess_list:
        new_list.append(state)
"""

pandas.DataFrame(new_list).to_csv('States_Left_to_know.csv')

