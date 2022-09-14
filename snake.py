from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    # Creates an empty list and calls the create_snake function.
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    # Creates the initial 3 snake segments.
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle('square')
        new_segment.color('white')
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    # Adds another segment onto the end of the snake.
    def extend(self):
        self.add_segment(self.segments[-1].position())

    # Continuously moves the snake.
    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    # Moves the snake in a direction but does not allow moving backwards.
    def move_up(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(90)

    def move_down(self):
        if self.head.heading() == 0 or self.head.heading() == 180:
            self.head.setheading(270)

    def move_left(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(180)

    def move_right(self):
        if self.head.heading() == 90 or self.head.heading() == 270:
            self.head.setheading(0)
