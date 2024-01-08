from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.highscore = 0
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.write(f"Score: {self.current_score}, High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.current_score += 1
        self.clear()
        self.write(f"Score: {self.current_score}, High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.current_score > self.highscore:
            self.highscore = self.current_score
        self.log_to_highscore_file()
        self.current_score = 0

    def log_to_highscore_file(self):
        with open("highscore.txt", mode="r") as file:
            highscore = file.read()
            if self.highscore > int(highscore):
                with open("highscore.txt", mode="r") as file1:
                    file1.write(f"{self.highscore}")



    # def game_over(self):
    #     self.hideturtle()
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.shapesize(stretch_wid=1, stretch_len=1)
    #     self.write(f"Game over.", move=False, align=ALIGNMENT, font=FONT)
