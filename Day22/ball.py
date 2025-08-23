from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.new_x = 10
        self.new_y = 10
        self.move_speed = 0.1
        self.move()

    def move(self):
        x1 = self.xcor() + self.new_x
        y1 = self.ycor() + self.new_y
        self.goto(x1, y1)

    def bounce_y(self):
        self.new_y *= -1
        self.move()

    def bounce_x(self):
        self.new_x *= -1
        self.move()
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.bounce_x()
