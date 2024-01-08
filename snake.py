from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_main_body()
        self.head = self.segments[0]

    def create_main_body(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def left(self):
        if self.head.heading() == 0:
            return True
        else:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            return True
        else:
            self.head.setheading(0)

    def up(self):
        if self.head.heading() == 270:
            return True
        else:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() == 90:
            return True
        else:
            self.head.setheading(270)

    def position(self):
        return self.head.position()

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.speed("fastest")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def reset(self):
        for seg in self.segments:
            seg.hideturtle()
        self.segments.clear()
        self.create_main_body()
        self.head = self.segments[0]
