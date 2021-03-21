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

    myScreen.title("Snake Game")
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


def accept_speed_user_input():
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


def accept_continue_user_input():
    user_input = ""
    continue_ = ""
    while user_input not in ["YES", "Y", "NO", "N"]:
        user_input = myScreen.textinput("Continue Prompt", "Do you want to continue?").upper()

    if user_input == "YES" or user_input == "Y":
        continue_ = True
    elif user_input == "NO" or user_input == "N":
        continue_ = False

    return continue_


#########################################################################
## Main Code:

timeee= time.ctime()
print(timeee)

# Establish Game GUI:
myScreen = t.Screen()
myScreen.tracer(0)

screen_cursor = t.Turtle()
establish_game_gui()

game_over_cursor = t.Turtle()
game_over_cursor.ht()
game_over_cursor.color("white")

score = ScoreBoard()

# Update Screen Output
myScreen.update()

# Accept User Snake Speed Input
game_speed = accept_speed_user_input()

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
continue_game = True
while continue_game:
    myScreen.update()
    time.sleep(game_speed)
    snake.animate_motion()

    if snake.ate_food(food_position):
        score.current += 1
        score.update()
        snake.extend_body_length()
        food_position = food.update_food_location()

    game_over = snake.check_game_status()
    # If Player Loses
    if game_over:
        score.check_high_score()
        score.write_back_in_file()
        screen_cursor.setposition(0, -SCREEN_MARGIN)
        game_over_cursor.write("Game Over", move=False, align="center", font=("Calibri", 20, "bold"))
        continue_game = accept_continue_user_input()
        if continue_game:
            food_position = food.update_food_location()
            game_over_cursor.clear()
            snake.reset()
            myScreen.listen()

# Close Screen upon click
myScreen.exitonclick()
