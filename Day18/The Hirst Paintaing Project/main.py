import random
import turtle
from turtle import Turtle as tur, Screen as sc
turtle.colormode(255)

color_list = [(205, 153, 99), (225, 205, 103), (161, 55, 101), (113, 187, 213), (154, 31, 58)]
print(color_list)

tim = tur()
tim.color('red')
tim.pensize(7)
tim.speed('fastest')

number_of_dots = 100
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
tim.pendown()
for i in range(1, number_of_dots):
    tim.dot(20,random.choice(color_list))
    tim.penup()
    tim.forward(50)
    tim.pendown()
    if(i%10==0):
        tim.setheading(90)
        tim.penup()
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        tim.pendown()




s = sc()
s.exitonclick()