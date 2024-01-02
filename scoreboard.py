from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}", move=False, align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.hideturtle()
        self.goto(0, 0)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.write(f"Game over.", move=False, align=ALIGNMENT, font=FONT)
