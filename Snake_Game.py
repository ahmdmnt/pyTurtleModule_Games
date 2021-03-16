#########################################################################
## pyTitle :
##     __Snake Game__
##
## Done By : Ahmed Montasser
##    Date : 13, March, 2021
##


#########################################################################
## Imported Modules:
import turtle as t
from random import randint
import time

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
VALID_INPUTS = ["EASY", "MEDIUM", "HARD", "E", "M", "H"]
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


#########################################################################
## Defined Functions Code:
def establish_game_gui():
    myScreen.setup(SCREEN_XCOR, SCREEN_YCOR)
    myScreen.bgcolor("dark blue")

    screen_cursor.ht()
    screen_cursor.pensize(3)
    screen_cursor.penup()
    screen_cursor.speed("fastest")
    screen_cursor.pencolor("white")
    screen_cursor.setposition(x=0, y=(SCREEN_YCOR / 2) - (HEADER_MARGIN / 1.5))
    screen_cursor.write("- Snake Game -", move=False, align="center", font=("Calibri", 30, "bold"))
    screen_cursor.setposition(x=-((SCREEN_XCOR / 2) - SCREEN_MARGIN), y=(SCREEN_YCOR / 2) - HEADER_MARGIN)
    screen_cursor.pendown()
    screen_cursor.fd(SCREEN_XCOR - (2 * SCREEN_MARGIN))
    screen_cursor.rt(90)
    screen_cursor.fd(SCREEN_YCOR - HEADER_MARGIN - SCREEN_MARGIN)
    screen_cursor.rt(90)
    screen_cursor.fd(SCREEN_XCOR - (2 * SCREEN_MARGIN))
    screen_cursor.rt(90)
    screen_cursor.fd(SCREEN_YCOR - HEADER_MARGIN - SCREEN_MARGIN)
    screen_cursor.penup()


def init_game_score():
    score_cursor.ht()
    score_cursor.speed("fastest")
    score_cursor.pu()
    score_cursor.pencolor("white")
    score_cursor.setposition(x=((SCREEN_XCOR / 2) - SCREEN_MARGIN - 10), y=((SCREEN_YCOR / 2) - HEADER_MARGIN + 10))


def update_game_score(g_score):
    score_cursor.clear()
    score_cursor.write(f"Score: {g_score}", move=False, align="right", font=("Calibri", 14, "bold"))


def accept_user_input():
    user_input = ""
    speed = 0
    while user_input not in VALID_INPUTS:
        user_input = myScreen.textinput("Snake Speed Prompt", "Select Game Mode:\n(Easy, Medium, Hard)").upper()

    if user_input == "EASY" or user_input == "E":
        speed = 0.4
    elif user_input == "MEDIUM" or user_input == "M":
        speed = 0.2
    elif user_input == "HARD" or user_input == "H":
        speed = 0.08

    return speed


#########################################################################
## Main Code:

# Establish Game GUI:
myScreen = t.Screen()
myScreen.tracer(0)

screen_cursor = t.Turtle()
establish_game_gui()

score_cursor = t.Turtle()
init_game_score()

# Visualize Score
game_score = 0
update_game_score(game_score)

# Update Screen Output
myScreen.update()

# Accept User Snake Speed Input
game_speed = accept_user_input()

# Create Snake Object
snake = Snake()

# Configure Keys functionality
myScreen.onkeypress(snake.head_up, "Up")
myScreen.onkeypress(snake.head_down, "Down")
myScreen.onkeypress(snake.head_right, "Right")
myScreen.onkeypress(snake.head_left, "Left")

# Enable Screen Keys Listen
myScreen.listen()

# Create Food Object
food = Food()
food_position = food.update_food_location()

# Start Game Logic
game_over = False
while not game_over:
    myScreen.update()
    time.sleep(game_speed)
    snake.animate_motion()

    if snake.ate_food(food_position):
        game_score += 1
        update_game_score(game_score)
        snake.extend_body_length()
        food_position = food.update_food_location()

    game_over = snake.check_game_status()

# If Player Loses
if game_over:
    screen_cursor.setposition(0, -SCREEN_MARGIN)
    screen_cursor.write("Game Over", move=False, align="center", font=("Calibri", 20, "bold"))

# Close Screen upon click
myScreen.exitonclick()
