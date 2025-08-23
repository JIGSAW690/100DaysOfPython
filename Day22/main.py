from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)


l_paddle = Paddle((-380, 0))
r_paddle = Paddle((372, 0))
ball = Ball()
l_scoreboard = Scoreboard((-200, 250))
r_scoreboard = Scoreboard((200, 250))


screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Check if ball is out of bounds for right paddle
    if ball.xcor() > 372:
        ball.reset_position()
        l_scoreboard.update_score()

    # Check if ball is out of bounds for left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        r_scoreboard.update_score()


screen.exitonclick()