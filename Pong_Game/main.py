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
## Main Code:

# Create the Pong Game Object
pong = PongGame()

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
    t.sleep(pong.ball_speed)
    pong.check_hit_paddle()
    winner = pong.check_hit_wall()      ## "None" if hit TOP/BOTTOM Walls, "Value" if hit RIGHT/LEFT Walls.
    if winner is not None:
        pong.update_players_score(winner)
        pong.reset_ball_position()
        pong.screen.update()
        t.sleep(3)

# Close Screen upon click
pong.screen.exitonclick()
