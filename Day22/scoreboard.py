from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.pencolor('white')
        self.penup()
        self.goto(position)
        self.write(f'{self.score}', position, align='center', font=('Arial', 20, 'bold'))

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f'{self.score}',  align='center', font=('Arial', 20, 'bold'))

