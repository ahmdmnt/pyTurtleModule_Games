#########################################################################
## pyTitle :
##     __Snake Game Main Code__
##
## Done By : Ahmed Montasser
##    Date : 13, March, 2021
##


#########################################################################
## Imported Modules:
from Snake_Game import *
import turtle as t
import time

#########################################################################
## Constants:
VALID_INPUTS = ["EASY", "MEDIUM", "HARD", "E", "M", "H"]


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
