#########################################################################
## pyTitle :
##     __Crossing Road Game Main Code__
##
## Done By : Ahmed Montasser
##    Date : 18, March, 2021
##


#########################################################################
## Imported Modules:
from CrossingRoad_Game import *
import time as t


#########################################################################
## Main Code:

game = GameGUI()
turtle = GameTurtle()
car_manager = GameCarsManager()
game_speed = 0.1

# Configure Keyboard Functionalities
game.screen.onkeypress(turtle.move_turtle_fw, "Up")
game.screen.onkeypress(turtle.move_turtle_bw, "Down")

# Enable Screen Keyboard Listener
game.screen.listen()

# Start Game Logic
game_over = False
while not game_over:
    t.sleep(game.speeed)
    game.screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    game_over = car_manager.collide_with_turtle(turtle)
    winner = turtle.check_if_wins()
    if winner:
        game.screen.update()
        # This method is created to reduce car_manager car objects created to optimize Size reserved \\...
        car_manager.passed_away_cars_cleanup()
        turtle.reset_position()
        game.update_level()
        t.sleep(0.5)

# Refresh Screen to Visualize where the Turtle loses Game
game.screen.update()
game.game_over()

# Exit Game on Screen Click
game.screen.exitonclick()