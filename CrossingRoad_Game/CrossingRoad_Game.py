#########################################################################
## pyTitle :
##     __Crossing Road Game Module__
##
## Done By : Ahmed Montasser
##    Date : 18, March, 2021
##


#########################################################################
## Imported Modules:
from turtle import Turtle, Screen
import random as rand


#########################################################################
## Constants:
SCREEN_X = 800
SCREEN_Y = 600
GAME_TITLE_POSITION = (-380, 240)
START_SIGN = [(-50, -215), (-50, -225)]
FINISH_SIGN = [(-50, 215), (-50, 225)]
LEVELBOARD_POSITION = (380, 210)
TURTLE_START_Y_POSITION = -230
TURTLE_END_Y_POSITION = 220
LANES = [-175, -125, -75, -25, 25, 75, 125, 175]
CAR_MOVE_DISTANCE = 10
CAR_COLORS = ["maroon", "black", "midnight blue", "gold", "saddle brown", "indigo"]


#########################################################################
## Game Classes:
class GameGUI:
    def __init__(self):
        self.screen = Screen()
        self.main_cursor = Turtle()
        self.level_cursor = Turtle()
        self.speeed = 0.1
        self.level = 1
        self.init_screen_configs()

    def init_screen_configs(self):
        self.screen.tracer(0)
        self.screen.setup(SCREEN_X, SCREEN_Y)
        # Enter Taskbar Title
        self.screen.title("Crossing Road Game")
        self.screen.bgcolor("gainsboro")
        self.main_cursor.speed("fastest")
        self.main_cursor.ht()
        self.main_cursor.pu()
        # Enter Game Title
        self.main_cursor.setposition(GAME_TITLE_POSITION)
        self.main_cursor.write(".:Crossing Road:.", move=False, align="left", font=("Calibri", 30, "bold"))
        # Draw Game Roads borders
        self.main_cursor.pensize(3)
        self.main_cursor.color("dim grey")
        for x in [-200, -150, -100, -50, 0, 50, 100, 150, 200]:
            self.main_cursor.pu()
            self.main_cursor.setposition(-410, x)
            self.main_cursor.pd()
            self.main_cursor.fd(820)
        # Draw Game Roads Dotted lines
        self.main_cursor.pensize(2)
        self.main_cursor.color("silver")
        for x in LANES:
            self.main_cursor.pu()
            self.main_cursor.setposition(-410, x)
            for i in range(int(820/15)):
                if i % 2 == 0:
                    self.main_cursor.pd()
                else:
                    self.main_cursor.pu()
                self.main_cursor.fd(15)
        # Draw Start Sign
        self.main_cursor.pu()
        self.main_cursor.shape("square")
        self.main_cursor.shapesize(0.5)
        self.main_cursor.setheading(0)
        self.main_cursor.showturtle()
        self.main_cursor.setposition(START_SIGN[0])
        for i in range(11):
            if i % 2 == 0:
                self.main_cursor.color("black")
                self.main_cursor.stamp()
            else:
                self.main_cursor.color("white")
                self.main_cursor.stamp()
            self.main_cursor.fd(10)
        self.main_cursor.setposition(START_SIGN[1])
        for i in range(11):
            if i % 2 == 0:
                self.main_cursor.color("white")
                self.main_cursor.stamp()
            else:
                self.main_cursor.color("black")
                self.main_cursor.stamp()
            self.main_cursor.fd(10)
        self.main_cursor.ht()
        # Draw Finish Sign
        self.main_cursor.pu()
        self.main_cursor.shape("square")
        self.main_cursor.shapesize(0.5)
        self.main_cursor.setheading(0)
        self.main_cursor.showturtle()
        self.main_cursor.setposition(FINISH_SIGN[1])
        for i in range(11):
            if i % 2 == 0:
                self.main_cursor.color("black")
                self.main_cursor.stamp()
            else:
                self.main_cursor.color("white")
                self.main_cursor.stamp()
            self.main_cursor.fd(10)
        self.main_cursor.setposition(FINISH_SIGN[0])
        for i in range(11):
            if i % 2 == 0:
                self.main_cursor.color("white")
                self.main_cursor.stamp()
            else:
                self.main_cursor.color("black")
                self.main_cursor.stamp()
            self.main_cursor.fd(10)
        self.main_cursor.ht()
        # Init Score Cursor
        self.level_cursor.shape("square")
        self.level_cursor.ht()
        self.level_cursor.pu()
        self.level_cursor.color("black")
        self.level_cursor.setposition(LEVELBOARD_POSITION)
        self.level_cursor.write(f"Level: {self.level}", move=False, align="right", font=("Courier", 18, "bold"))

    def update_level(self):
        self.level += 1
        self.speeed *= 0.75
        self.level_cursor.clear()
        self.level_cursor.write(f"Level: {self.level}", move=False, align="right", font=("Courier", 18, "bold"))

    def game_over(self):
        self.level_cursor.setposition(0, 0)
        self.level_cursor.write("GAME OVER", move=False, align="center", font=("Calibri", 28, "bold"))

class GameTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.fillcolor("olive")
        self.pu()
        self.shapesize(1.5)
        self.setheading(90)
        self.setposition(0, -230)

    def reset_position(self):
        self.setposition(0, TURTLE_START_Y_POSITION)

    def move_turtle_fw(self):
        if self.ycor() < TURTLE_END_Y_POSITION:
            self.forward(50)

    def move_turtle_bw(self):
        if self.ycor() > TURTLE_START_Y_POSITION:
            self.backward(50)

    def check_if_wins(self):
        if self.ycor() == TURTLE_END_Y_POSITION:
            return True
        else:
            return False


class GameCarsManager:
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        dice = rand.randint(1, 6)
        if dice == 3:
            new_car = Turtle("square")
            new_car.shapesize(1, 2)
            new_car.pu()
            new_car.color(rand.choice(CAR_COLORS))
            new_car.setposition(410, rand.choice(LANES))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(CAR_MOVE_DISTANCE)

    def passed_away_cars_cleanup(self):
        print("Total Car Count:", len(self.all_cars))
        for index, car in enumerate(self.all_cars):
            if car.xcor() < 0:
                car.ht()
                del self.all_cars[index]
        print("After Cleanup Count:", len(self.all_cars),"\n")

    def collide_with_turtle(self, turtle):
        for car in self.all_cars:
            if car.distance(turtle) <= 30:
                return True
        return False