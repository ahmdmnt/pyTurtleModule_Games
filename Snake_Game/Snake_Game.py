#########################################################################
## pyTitle :
##     __Snake Game Module__
##
## Done By : Ahmed Montasser
##    Date : 13, March, 2021
##


#########################################################################
## Imported Modules:
import turtle as t
from random import randint

#########################################################################
## Constants:
HEADING = {
    "UP": 90.0,
    "DOWN": 270.0,
    "RIGHT": 0.0,
    "LEFT": 180.0
}
SCREEN_XCOR = 700
SCREEN_YCOR = 700
SCREEN_MARGIN = 20
HEADER_MARGIN = 130
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
SNAKE_STEP = 20
HEAD = 0


#########################################################################
## Snake Class:
class Snake:
    def __init__(self):
        self.body = []
        for position in STARTING_POSITIONS:
            segment = t.Turtle("square")
            segment.shapesize(0.9)
            segment.color("white")
            segment.pu()
            segment.setposition(position)
            self.body.append(segment)

    def animate_motion(self):
        for index in range(len(self.body) - 1, 0, -1):
            prev_segment_position = self.body[index - 1].position()
            self.body[index].setposition(prev_segment_position)
        self.body[HEAD].forward(SNAKE_STEP)


    def head_up(self):
        if self.body[HEAD].heading() != HEADING["DOWN"]:
            self.body[HEAD].setheading(HEADING["UP"])


    def head_down(self):
        if self.body[HEAD].heading() != HEADING["UP"]:
            self.body[HEAD].setheading(HEADING["DOWN"])


    def head_right(self):
        if self.body[HEAD].heading() != HEADING["LEFT"]:
            self.body[HEAD].setheading(HEADING["RIGHT"])


    def head_left(self):
        if self.body[HEAD].heading() != HEADING["RIGHT"]:
            self.body[HEAD].setheading(HEADING["LEFT"])


    def check_game_status(self):
        g_over = False

        # Check if the Snake hit a wall,
        if (self.body[HEAD].xcor() >= ((SCREEN_XCOR/2)-SCREEN_MARGIN)) \
                or (self.body[HEAD].xcor() <= -((SCREEN_XCOR/2)-SCREEN_MARGIN)):
            g_over = True
        elif (self.body[HEAD].ycor() >= ((SCREEN_YCOR/2)-HEADER_MARGIN)) \
                or (self.body[HEAD].ycor() <= -((SCREEN_YCOR/2)-SCREEN_MARGIN)):
            g_over = True

        # Check if the Snake hit itself,
        for segment in self.body[1:]:
            if self.body[HEAD].distance(segment) <= 10:
                g_over = True

        return g_over


    def ate_food(self, f_position):
        if self.body[HEAD].distance(f_position) <= 13:
            return True
        else:
            return False


    def extend_body_length(self):
        tail_position = self.body[-1].position()
        segment = t.Turtle("square")
        segment.shapesize(0.9)
        segment.color("white")
        segment.pu()
        segment.setposition(tail_position)
        self.body.append(segment)


## Food Class:
class Food:
    def __init__(self):
        self.piece = t.Turtle("circle")
        self.piece.pu()
        self.piece.shapesize(0.8)
        self.piece.color("yellow")

    def update_food_location(self):
        x_position = randint(int(-((SCREEN_XCOR / 2) - SCREEN_MARGIN-50)), int((SCREEN_XCOR / 2) - SCREEN_MARGIN-50))
        y_position = randint(int(-((SCREEN_YCOR/2)-SCREEN_MARGIN-50)), int((SCREEN_YCOR/2)-HEADER_MARGIN-50))
        self.piece.setposition(x_position, y_position)
        position = (x_position, y_position)
        return position
