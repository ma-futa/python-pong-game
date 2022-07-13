from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,position ):
        super().__init__()
        self.shapesize(stretch_wid=5 ,stretch_len=1,outline=1)
        self.penup()
        self.speed('fastest')
        self.color('white')
        self.shape('square')
        self.goto(x=position, y=0)

    def go_up(self):
        self.goto(self.xcor(), self.ycor() + 20)

    def go_down(self):
        self.goto(self.xcor(), self.ycor() - 20)



