import turtle as t

timmy = t.Turtle()
timmy.shape('turtle')
timmy.color('red')

"""
Draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon & decagon {ALL_IN_ONE}, 
each with different colour using the configured turtle
"""

sides = range(3,11)
colors = ['brown','yellow','red','blue','pink','green','purple','black']
count = 0

def create_figure(ang):
    timmy.forward(100)
    timmy.right(ang)

for side in sides:
    timmy.color(colors[count])
    for _ in range(side):
        create_figure(360/side)
    count += 1

screen = t.Screen()
screen.exitonclick()