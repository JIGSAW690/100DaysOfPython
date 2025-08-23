from turtle import Turtle, Screen
import random

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_names = ['tim', 'jenny', 'bob', 'marley', 'kohinoor', 'baba']
y_cor = [-70, -40, -10, 20, 50, 80]
screen = Screen()
screen.setup(width=500, height=400)
is_race_on = False
turtle_obj_list = []

def create_turtle(name, color, x, y):
    name = Turtle(shape='turtle')
    name.color(color)
    name.penup()
    name.goto(x=x, y=y)
    name.pendown()
    turtle_obj_list.append(name)

user_choice = screen.textinput(title='Make your bet', prompt='Which turtle will win the race?')
for i in range(6):
    create_turtle(turtle_names[i],colors[i],-230,y_cor[i])

if user_choice:
    is_race_on = True

while(is_race_on):
    for turtle in turtle_obj_list:
        if(turtle.xcor()>230):
            is_race_on = False
            if(turtle.pencolor==user_choice):
                print(f"You have won! {turtle.pencolor} turtle is the winner.")
            else:
                print(f"You have lost! {turtle.pencolor} turtle is the winner.")
        random_dist = random.randint(1,10)
        turtle.forward(random_dist)




screen.exitonclick()
