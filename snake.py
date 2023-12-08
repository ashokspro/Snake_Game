from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
FORWARD_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for positions in START_POSITIONS:
            self.add_segment(positions)

    def add_segment(self, positions):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(positions)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            x_position = self.segments[seg - 1].xcor()
            y_position = self.segments[seg - 1].ycor()
            self.segments[seg].goto(x_position, y_position)
        self.head.forward(FORWARD_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
