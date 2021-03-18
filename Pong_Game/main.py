#########################################################################
## pyTitle :
##     __Pong Game Main Code__
##
## Done By : Ahmed Montasser
##    Date : 16, March, 2021
##


#########################################################################
## Imported Modules:
from Pong_Game import *
import time as t


#########################################################################
## Constants:
VALID_INPUTS = ["EASY", "MEDIUM", "HARD", "E", "M", "H"]


#########################################################################
## Defined Functions Code:
def accept_user_input():
    user_input = ""
    speed = 0
    while user_input not in VALID_INPUTS:
        user_input = pong.screen.textinput("Game Speed Prompt", "Select Game Mode:\n(Easy, Medium, Hard)").upper()

    if user_input == "EASY" or user_input == "E":
        speed = 0.11
    elif user_input == "MEDIUM" or user_input == "M":
        speed = 0.08
    elif user_input == "HARD" or user_input == "H":
        speed = 0.04

    return speed


#########################################################################
## Main Code:

# Create the Pong Game Object
pong = PongGame()

# Accept User Snake Speed Input
game_speed = accept_user_input()

# Configure Keyboard Keys Functionalities
pong.screen.onkeypress(pong.move_rt_paddle_up, "Up")
pong.screen.onkeypress(pong.move_rt_paddle_down, "Down")
pong.screen.onkeypress(pong.move_lt_paddle_up, "w")
pong.screen.onkeypress(pong.move_lt_paddle_down, "s")

# Start Screen to listen for Keyboard clicks
pong.screen.listen()


# Game Logic
game_over = False
while not game_over:
    pong.move_ball()
    pong.screen.update()
    t.sleep(game_speed)
    pong.check_hit_paddle()
    winner = pong.check_hit_wall()      ## "None" if hit TOP/BOTTOM Walls, "Value" if hit RIGHT/LEFT Walls.
    if winner is not None:
        pong.update_players_score(winner)
        pong.ball.setposition(0, 0)
        pong.screen.update()
        t.sleep(3)

# Close Screen upon click
pong.screen.exitonclick()
