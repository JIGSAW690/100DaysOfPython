from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 1
        self.color("White")
        self.pencolor('White')
        self.hideturtle()
        self.penup()
        self.goto(-215, 250)
        self.display_score()

    def display_score(self ):
        self.write(f'Level: {self.score}', align='center', font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(0, 0)
        self.clear()
        self.write(f'Game Over! -- Score: {self.score}', align='center', font=FONT)
