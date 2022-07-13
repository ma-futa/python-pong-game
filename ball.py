from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('purple')
        # self.speed('slow')
        self.penup()
        self.y_direction = True
        self.x_direction = True

    def move(self):
        if self.ycor() > 250:
            self.y_direction = False
        if self.ycor() < -250:
            self.y_direction = True

        if self.xcor() > 350:
            self.x_direction = False
        if self.xcor() < -350:
            self.x_direction = True

        if self.y_direction:
            new_y = self.ycor() + 10
        else:
            new_y = self.ycor() - 10

        if self.x_direction:
            new_x = self.xcor() + 10
        else:
            new_x = self.xcor() - 10
        self.goto(new_x,new_y)