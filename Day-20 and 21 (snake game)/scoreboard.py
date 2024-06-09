from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_soceboard()

    def update_soceboard(self):
        self.write(f"Score:{self.score}", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self, increase_score):
        self.score += increase_score
        self.clear()
        self.update_soceboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align=ALIGNMENT, font=FONT)