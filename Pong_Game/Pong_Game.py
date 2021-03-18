#########################################################################
## pyTitle :
##     __Pong Game Module__
##
## Done By : Ahmed Montasser
##    Date : 16, March, 2021
##


#########################################################################
## Imported Modules:
from turtle import Turtle, Screen

#########################################################################
## Constants:
SCREEN_XCOR = 900
SCREEN_YCOR = 740
GAME_XCOR = 800
GAME_YCOR = 600
Y_MARGIN = 70
X_MARGIN = 50
LT_PADDLE_POSITION = (-(GAME_XCOR/2 - 20), 0)
RT_PADDLE_POSITION = ((GAME_XCOR/2 - 20), 0)
LT_PLAYER = 0
RT_PLAYER = 1


#########################################################################
## Game Classes:
class PongGame:
    def __init__(self):
        # Create the Screen Object
        self.screen = Screen()
        self.screen.setup(SCREEN_XCOR, SCREEN_YCOR)
        self.screen.bgcolor("black")
        # Create Screen Cursor; Draw Pong Game Layout
        self.screen_cursor = Turtle()
        self.screen_cursor.ht()
        self.establish_game_layout()
        self.screen.tracer(0)

        # Create Score Cursor; Visualize and Update the Score
        self.score_cursor = Turtle()
        self.score_cursor.ht()
        self.score_cursor.color("white")
        self.score_cursor.speed("fastest")
        self.score_cursor.pu()
        self.scores = [0, 0]
        self.update_players_score()

        # Create Paddles Objects
        self.rt_paddle = Turtle()
        self.lt_paddle = Turtle()
        self.init_paddle(LT_PADDLE_POSITION, RT_PADDLE_POSITION)

        # Create Ball Object
        self.ball = Turtle()
        self.x_move = 10
        self.y_move = 10
        self.init_ball()

    def establish_game_layout(self):
        self.screen.title("Pong Game")
        self.screen_cursor.color("white")
        self.screen_cursor.pensize(3)
        self.screen_cursor.penup()
        self.screen_cursor.speed("fastest")
        # Type Game Title
        self.screen_cursor.setposition(x=0, y=(SCREEN_YCOR/2 - Y_MARGIN/1.3))
        self.screen_cursor.write("- Pong Game -", move=False, align="center", font=("Calibri", 30, "bold"))
        # Draw the Pong Table Margins
        self.screen_cursor.setposition((-GAME_XCOR/2), (GAME_YCOR/2))
        self.screen_cursor.pd()
        self.screen_cursor.fd(GAME_XCOR)
        self.screen_cursor.rt(90)
        self.screen_cursor.fd(GAME_YCOR)
        self.screen_cursor.rt(90)
        self.screen_cursor.fd(GAME_XCOR)
        self.screen_cursor.rt(90)
        self.screen_cursor.fd(GAME_YCOR)
        # Draw Dotted line
        self.screen_cursor.pu()
        self.screen_cursor.pensize(1)
        self.screen_cursor.setposition(0, (GAME_YCOR/2))
        self.screen_cursor.setheading(270)
        for i in range(int(GAME_YCOR/10)):
            if i % 2 == 0:
                self.screen_cursor.pd()
            else:
                self.screen_cursor.pu()
            self.screen_cursor.fd(10)

    def update_players_score(self, index=None):
        if index is not None:
            self.scores[index] += 1
        self.score_cursor.clear()
        self.score_cursor.setposition(-50, (GAME_YCOR/2)-70)
        self.score_cursor.write(f"{self.scores[LT_PLAYER]}", move=False, align="center", font=("Courier", 40, "bold"))
        self.score_cursor.setposition(50, (GAME_YCOR/2)-70)
        self.score_cursor.write(f"{self.scores[RT_PLAYER]}", move=False, align="center", font=("Courier", 40, "bold"))

    def init_paddle(self, lt_paddle_position, rt_paddle_position):
        self.lt_paddle.shape("square")
        self.lt_paddle.pu()
        self.lt_paddle.setheading(90)
        self.lt_paddle.shapesize(1, 6)
        self.lt_paddle.color("white")
        self.lt_paddle.setposition(lt_paddle_position)
        self.rt_paddle.shape("square")
        self.rt_paddle.pu()
        self.rt_paddle.setheading(90)
        self.rt_paddle.shapesize(1, 6)
        self.rt_paddle.color("white")
        self.rt_paddle.setposition(rt_paddle_position)

    def init_ball(self):
        self.ball.shape("circle")
        self.ball.pu()
        self.ball.shapesize(1.5, 1.5)
        self.ball.color("lime")

    def move_rt_paddle_up(self):
        if self.rt_paddle.ycor() <= (GAME_YCOR/2 - 80):
            self.rt_paddle.forward(20)

    def move_rt_paddle_down(self):
        if self.rt_paddle.ycor() >= -(GAME_YCOR/2 - 80):
            self.rt_paddle.backward(20)

    def move_lt_paddle_up(self):
        if self.lt_paddle.ycor() <= (GAME_YCOR/2 - 80):
            self.lt_paddle.forward(20)

    def move_lt_paddle_down(self):
        if self.lt_paddle.ycor() >= -(GAME_YCOR/2 - 80):
            self.lt_paddle.backward(20)

    def move_ball(self):
        self.ball.goto((self.ball.xcor()+self.x_move), (self.ball.ycor()+self.y_move))

    def bounce_ball_yAxis(self):
        self.y_move *= -1

    def bounce_ball_xAxis(self):
        self.x_move *= -1

    def check_hit_wall(self):
        if self.ball.xcor() >= (GAME_XCOR/2 - 10):
            return LT_PLAYER
        elif self.ball.xcor() <= -(GAME_XCOR/2 - 10):
            return RT_PLAYER

        if self.ball.ycor() >= (GAME_YCOR/2 - 30) or \
                self.ball.ycor() <= -(GAME_YCOR/2 - 30):
            self.bounce_ball_yAxis()
            return None

    def check_hit_paddle(self):
        if self.ball.distance(self.rt_paddle) < 60 and self.ball.xcor() > 340 or \
                self.ball.distance(self.lt_paddle) < 60 and self.ball.xcor() < -340:
            self.bounce_ball_xAxis()
