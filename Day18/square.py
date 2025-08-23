from turtle import Turtle as t

timmy = t()
timmy.shape('turtle')
timmy.color('red')

#Print a square using the configured Turtle object
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)
