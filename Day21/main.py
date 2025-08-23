from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from score_board import Scoreboard

game_on = True

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title('THE SNAKE GAME')
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

while(game_on):
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect Collision with food.
    if snake.head.distance(food) < 15:
        food.move_randomly()
        score_board.increase_score()
        snake.extend_snake()

    #Detect collision with walls
    if snake.head.xcor() == 300 or snake.head.xcor() == -300 or snake.head.ycor() == 300 or snake.head.ycor() == -300:
        game_on = False
        score_board.game_over()

    #Detect collision with snake's own body
    for segment in snake.segments:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_on = False
            score_board.game_over()



screen.exitonclick()