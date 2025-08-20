from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')

GAME_OVER_FONT = ('Courier', 30, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.r_score = 0
        self.l_score = 0
        self.goto(x=0, y=260)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f'{self.l_score} | {self.r_score}', align=ALIGNMENT, font=FONT)

    def increase_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def increase_l_score(self):
        self.l_score += 1
        self.update_scoreboard()
