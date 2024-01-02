from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.penup()
        self.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))

    def change_location(self):
        self.goto(random.randrange(-280, 280, 20), random.randrange(-280, 280, 20))

    # def position(self):
    #     return self.position()
    #
    # def remove(self):
    #     self.hideturtle()


