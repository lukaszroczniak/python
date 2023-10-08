from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.is_at_start()
        self.speed("fastest")
        self.shape("turtle")
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def is_at_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finish(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
