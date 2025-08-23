from turtle import Turtle as t

timmy = t()
timmy.shape('turtle')
timmy.color('red')

# Draw a dashed line using the configured turtle
for _ in range(20):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()
