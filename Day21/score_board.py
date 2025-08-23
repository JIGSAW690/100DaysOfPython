from turtle import Turtle

FONT = ('Arial', 12, 'bold')
ALIGNMENT = 'center'

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 280)
        self.pencolor('white')
        self.hideturtle()
        self.update_score()

    def update_score(self):
        self.write(f'Score: {self.score}', False, ALIGNMENT, FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write('GAME OVER', False, ALIGNMENT, FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()