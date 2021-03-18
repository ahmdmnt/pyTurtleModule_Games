#########################################################################
## pyTitle :
##     __Turtle Race Game__
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
COLOR = 1
INDEX = 0
RACING_TURTLES = {
    0: "red",
    1: "grey",
    2: "blue",
    3: "black",
    4: "purple",
    5: "orange",
    6: "pink"
}


#########################################################################
## Defined Functions Code:
def establish_game_gui(t_cursor):
    t_cursor.ht()
    t_cursor.pensize(3)
    t_cursor.penup()
    t_cursor.speed("fastest")
    t_cursor.setposition(x=0, y=300)
    t_cursor.write("-Turtle Race-", move=False, align="center", font=("Calibri", 24, "bold"))
    t_cursor.setposition(x=-430, y=290)
    t_cursor.pendown()
    t_cursor.fd(860)
    t_cursor.rt(90)
    t_cursor.fd(620)
    t_cursor.rt(90)
    t_cursor.fd(860)
    t_cursor.rt(90)
    t_cursor.fd(620)


#########################################################################
## Main Code:

# Establish Game GUI:
myScreen = t.Screen()
myScreen.setup(900, 700)
cursor = t.Turtle()
establish_game_gui(cursor)
cursor.penup()

# Create Racing Turtles,,
racing_turtles = []
init_y_position = 340
for i_tur in RACING_TURTLES.items():
    temp_turtle = t.Turtle()
    temp_turtle.shape("turtle")
    temp_turtle.shapesize(3)
    temp_turtle.pu()
    temp_turtle.color(i_tur[COLOR])
    init_y_position -= 90
    temp_turtle.setposition(-400, init_y_position)
    racing_turtles.append(temp_turtle)

# Ask user to choose his/her own turtle,,
user_input = myScreen.textinput("User Input Prompt", "Choose from list your turtle color:\n"
                                                     "(red - grey - blue - black - purple - orange - pink)")

# Start Race,,
race_finished = False
while not race_finished:
    for ind, tur in enumerate(racing_turtles):
        pace = randint(5, 15)
        tur.fd(pace)
        print(RACING_TURTLES[ind], ":", tur.xcor())
        if tur.xcor() >= 370:

            race_finished = True
            cursor.setposition(x=0, y=0)
            if RACING_TURTLES[ind] == user_input:
                cursor.write("WOOO!! You Won.", move=False, align="center", font=("Calibri", 18, "bold"))
            else:
                cursor.write("NAAH!! You Lose.", move=False, align="center", font=("Calibri", 18, "bold"))
            cursor.setposition(x=0, y=-30)
            cursor.write(f"Winner is: {RACING_TURTLES[ind]}", move=False, align="center", font=("Calibri", 18, "bold"))
            break

# Close Screen upon click
myScreen.exitonclick()
