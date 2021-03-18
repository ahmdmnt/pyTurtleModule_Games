#########################################################################
## pyTitle :
##     __Etch a Sketch Game__
##
## Done By : Ahmed Montasser
##    Date : 12, March, 2021
##


#########################################################################
## Imported Modules:

import turtle as t


#########################################################################
## Constants:
DISTANCE = 10
ANGLE = 10

## Global Variables:
drawCursor = t.Turtle()


#########################################################################
## Defined Functions Code:

def move_forward():
    drawCursor.forward(DISTANCE)


def move_backward():
    drawCursor.backward(DISTANCE)


def head_cw():
    drawCursor.left(ANGLE)


def head_ccw():
    drawCursor.right(ANGLE)


def clear_drawings():
    drawCursor.speed("fastest")
    drawCursor.setposition(0, 0)
    drawCursor.clear()
    drawCursor.setheading(0)
    drawCursor.speed("normal")



def establish_game_gui(t_cursor):
    t_cursor.ht()
    t_cursor.pensize(3)
    t_cursor.penup()
    t_cursor.speed("fastest")
    t_cursor.setposition(x=0, y=300)
    t_cursor.write("Etch a Sketch", move=False, align="center", font=("Calibri", 24, "bold"))
    t_cursor.setposition(x=-430, y=280)
    t_cursor.pendown()
    t_cursor.fd(860)
    t_cursor.rt(90)
    t_cursor.fd(600)
    t_cursor.rt(90)
    t_cursor.fd(860)
    t_cursor.rt(90)
    t_cursor.fd(600)


#########################################################################
## Main Code:

# Establish Game GUI:
myScreen = t.Screen()
myScreen.setup(900, 700)
cursor = t.Turtle()
establish_game_gui(cursor)

# Configure Keys Functionalities
myScreen.onkeypress(move_forward, "Up")
myScreen.onkeypress(move_backward, "Down")
myScreen.onkeypress(head_ccw, "Right")
myScreen.onkeypress(head_cw, "Left")
myScreen.onkeypress(clear_drawings, "c")

# Enable Screen Keys Listener
myScreen.listen()

# Close Screen upon click
myScreen.exitonclick()
