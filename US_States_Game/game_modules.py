from turtle import Turtle, Screen


class ScreenCursor:
    def __init__(self):
        self.screen = Screen()
        self.screen.tracer(0)
        self.screen.title("U.S. States Game")
        self.screen.setup(725, 632)
        self.screen.bgpic("blank_states_img.gif")
        ##-------------------------------------------
        self.main_cursor = Turtle()
        self.main_cursor.ht()
        self.main_cursor.pu()
        self.display_game_title()
        ##-------------------------------------------
        self.message_cursor = Turtle()
        self.message_cursor.ht()
        self.message_cursor.pu()
        self.message_cursor.color("black")
        ##-------------------------------------------
        self.state_cursor = Turtle()
        self.state_cursor.ht()
        self.state_cursor.pu()
        self.state_cursor.color("black")


    def display_game_title(self):
        self.main_cursor.color("black")
        self.main_cursor.setposition(160, 267)
        self.main_cursor.write("U.S. States Game", move=False, align="center", font=("Verdana", 28, "bold"))
        self.main_cursor.color("grey")
        self.main_cursor.setposition(210, 252)
        self.main_cursor.write(f"How well do you memorize US States?",
                               move=False, align="center", font=("Verdana", 10, "italic"))

    def display_game_title(self):
        self.main_cursor.color("black")
        self.main_cursor.setposition(160, 267)
        self.main_cursor.write("U.S. States Game", move=False, align="center", font=("Verdana", 28, "bold"))
        self.main_cursor.color("grey")
        self.main_cursor.setposition(210, 252)
        self.main_cursor.write(f"How well do you memorize US States?",
                               move=False, align="center", font=("Verdana", 10, "italic"))

    def display_welcome_message(self, x_position):
        self.message_cursor.clear()
        self.message_cursor.setposition(x_position, 0)
        self.message_cursor.write("Welcome to U.S. States Game",
                                  move=False, align="center", font=("Verdana", 18, "bold"))

    def display_input(self, message):
        self.message_cursor.clear()
        self.message_cursor.setposition(-350, -243)
        self.message_cursor.write(message,
                                  move=False, align="left", font=("Courier", 14, "bold"))

    def display_state_name(self, state_name, x_position, y_position):
        self.state_cursor.setposition(x_position, y_position)
        self.state_cursor.write(state_name, move=False, align="center", font=("Verdana", 8, "bold"))


class Score:
    def __init__(self):
        self.value = 0
        self.lose_count = 8
        self.player_life = []
        self.init_player_life()
        self.cursor = Turtle()
        self.cursor.ht()
        self.cursor.pu()
        self.print()

    def init_player_life(self):
        x_cor = -365
        for i in range(self.lose_count):
            x_cor += 25
            temp = Turtle("square")
            # temp.shapesize(2, 1)
            temp.pu()
            temp.color("red")
            temp.setposition(x_cor, -290)
            self.player_life.append(temp)

        temp = Turtle()
        temp.ht()
        temp.pu()
        temp.color("gray")
        temp.setposition(-348, -276)
        temp.write(f"PLAYER LIFE BAR:", move=False, align="left", font=("Verdana", 10, "normal"))



    def update(self):
        self.value += 1

    def player_lose(self):
        self.lose_count -= 1
        self.player_life[self.lose_count].ht()
        if self.lose_count == 0:
            return True
        else:
            return False

    def player_win(self):
        if self.value == 50:
            return True
        else:
            return False

    def print(self):
        self.cursor.clear()
        if self.value < 10:
            score_output = f"0{self.value}/50"
        else:
            score_output = f"{self.value}/50"
        self.cursor.color("grey")
        self.cursor.setposition(330, -270)
        self.cursor.write(f"SCORE", move=False, align="right", font=("Verdana", 10, "normal"))
        self.cursor.color("black")
        self.cursor.setposition(340, -312)
        self.cursor.write(score_output, move=False, align="right", font=("Arial", 30, "bold"))
