#########################################################################
## pyTitle :
##     __US States Game Main Code__
##  Usage of Pandas, OOP and Turtle.
##
## Done By : Ahmed Montasser
##    Date : 13, March, 2021
##


#########################################################################
## Imported Modules:
import turtle as t
import game_modules as gm
import pandas as pd
import time


#########################################################################
## Global Variable:


#########################################################################
## Defined Functions Code:
def init_button(button_color, center_x, center_y, width, height, corner_size):
    button.ht()
    button.color("white")
    button.speed(0)
    button.hideturtle()
    button.speed(0)
    button.up()
    button.hideturtle()
    button.up()
    button.goto(center_x - width / 2 + corner_size, center_y - height / 2)
    button.down()
    button.fillcolor(button_color)
    button.begin_fill()
    for _ in range(2):
        button.fd(width - 2 * corner_size)
        button.circle(corner_size, 90)
        button.fd(height - 2 * corner_size)
        button.circle(corner_size, 90)
    button.end_fill()
    button.pu()
    button.setposition(center_x, center_y - 15)
    button.write("PLAY QUIZ", move=False, align="center", font=("Verdana", 20, "bold"))


def button_is_clicked(x, y):
    global game_started
    if not game_started:
        if -350 < x < -150 and 258 < y < 303:
            print("Button CLicked!")
            game_started = True


#########################################################################
## Main Code:
game_gui = gm.ScreenCursor()
score = gm.Score()

button = t.Turtle()
init_button("lime green", -250, 280, 200, 50, 10)
game_gui.screen.onscreenclick(button_is_clicked, 1)

df = pd.read_csv("50_states.csv")
us_states = list(df.state)

game_started = False

x_cor = -550
while not game_started:
    game_gui.screen.update()
    if game_gui.message_cursor.xcor() >= 450:
        x_cor = -550
    x_cor += 30
    game_gui.display_welcome_message(x_cor)
    time.sleep(0.35)

game_gui.message_cursor.clear()

while game_started:
    game_gui.screen.update()
    user_input = game_gui.screen.textinput("Guess the States", "What's another state name?").title()

    if user_input in us_states:
        score.update()
        x_cor = int(df[df.state == user_input].x)
        y_cor = int(df[df.state == user_input].y)
        game_gui.display_state_name(user_input, x_cor, y_cor)
        if score.player_win():
            game_gui.display_input("Game Prompt: CONGRATZZZ!! ^^")
            break
        game_gui.display_input("Game Prompt: Correct Guess!")

    else:
        if score.player_lose():
            game_gui.display_input("Game Prompt: You Lose!! :S:S")
            break
        game_gui.display_input("Game Prompt: Wrong Input!")

    score.print()
    time.sleep(0.45)

game_gui.screen.update()

# Close Screen upon click
game_gui.screen.exitonclick()
