from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(20)
def move_backwards():
    tim.backward(20)
def move_clockwise():
    tim.setheading(tim.heading()+10)
def move_anti_clockwise():
    tim.setheading(tim.heading()-10)
def cs():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(move_anti_clockwise, 'a')
screen.onkey(move_clockwise, 'd')
screen.onkey(screen.clearscreen, 'c')
screen.exitonclick()