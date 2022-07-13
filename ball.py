from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('purple')
        # self.speed('slow')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        self.goto(self.xcor() + self.x_move,self.ycor()+self.y_move)

    def bounce(self):
        # if self.ycor() > 250 or self.ycor() < -250:
        self.y_move *= -1

        # if self.xcor() > 350 or self.xcor() < -350:
        #     self.x_move *= -1

