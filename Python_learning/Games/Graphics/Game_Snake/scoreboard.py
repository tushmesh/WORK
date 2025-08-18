from food import Food


class ScoreBoard(Food):
    total = 0
    def __init__(self):
        super().__init__()
        self.cal_score()

    def cal_score(self):
        self.clear()
        self.color("white")
        self.setposition(x=20, y=285)
        self.write(arg=self.total)
        self.total += 100
        self.hideturtle()

