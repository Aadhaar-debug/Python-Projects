from turtle import Turtle

class Paddle(Turtle):

    def __init__(self , position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(350, 0)

    def go_up(self):
        new_y = self.ycor() + 28
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 28
        self.goto(self.xcor(), new_y)