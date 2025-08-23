import random
import turtle as t
t.colormode(255)

tim = t.Turtle()
tim.speed('fastest')

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    col = (r,g,b)
    return col

def draw(gap):
    for _ in range(int(360/gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading()+gap)

draw(int(input('Enter distance between each circle in the Spyrograph?')))

screen = t.Screen()
screen.exitonclick()