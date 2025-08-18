from turtle import Turtle


class PongShape(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.shape("square")
        self.color("white")
        self.goto(position)

    def go_up(self):
        paddle_y_cor = self.ycor() + 20
        self.goto(self.xcor(), paddle_y_cor)

    def go_down(self):
        paddle_y_cor = self.ycor() - 20
        self.goto(self.xcor(), paddle_y_cor)
