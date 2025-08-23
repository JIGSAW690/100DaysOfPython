import random
import turtle as t
import random

timmy = t.Turtle()
t.colormode(255)
timmy.color('red')
timmy.shape('turtle')
timmy.pensize(15)
timmy.speed('fastest')

#colors = ['brown','yellow','red','blue','pink','green','purple','black']
direction = [0, 90, 180, 270]

def random_colors():
    r = random.randint(0, 255)
    g = random.randint(0,255)
    b = random.randint(0, 255)
    col = (r,g,b)
    return col

for _ in range(300):
    timmy.color(random_colors())
    timmy.forward(50)
    timmy.setheading(random.choice(direction))




