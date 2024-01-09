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
        self.get_highscore()
        self.write(f"Score: {self.current_score}, High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)

    def add_score(self):
        self.current_score += 1
        self.refresh()

    def reset(self):
        if self.current_score > self.highscore:
            self.highscore = self.current_score
        self.save_to_highscore()
        self.current_score = 0
        self.refresh()

    def save_to_highscore(self):
        with open("highscore.txt") as file:
            highscore = file.readlines()
            if self.highscore > int(highscore[0]):
                with open("highscore.txt", mode="w") as f:
                    f.writelines(f"{self.highscore}")

    def get_highscore(self):
        with open("highscore.txt") as file:
            highscore = file.readlines()
            if self.highscore < int(highscore[0]):
                self.highscore = int(highscore[0])
                self.refresh()

    def refresh(self):
        self.clear()
        self.write(f"Score: {self.current_score}, High Score: {self.highscore}", move=False, align=ALIGNMENT, font=FONT)



    # def game_over(self):
    #     self.hideturtle()
    #     self.goto(0, 0)
    #     self.color("white")
    #     self.shapesize(stretch_wid=1, stretch_len=1)
    #     self.write(f"Game over.", move=False, align=ALIGNMENT, font=FONT)
