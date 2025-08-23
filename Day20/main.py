from turtle import Turtle, Screen
import time
from Snake import Snake

game_on = True

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('THE SNAKE GAME')
screen.tracer(0)

snake = Snake()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while(game_on):
    screen.update()
    time.sleep(0.1)
    snake.move()



screen.exitonclick()