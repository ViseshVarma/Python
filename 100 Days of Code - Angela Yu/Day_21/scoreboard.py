from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("courier", 40, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("courier", 40, "normal"))

        # player names
        self.goto(-300, 200)
        self.write("Player 1", align="center", font=("courier", 20, "normal"))
        self.goto(300, 200)
        self.write("Player 2", align="center", font=("courier", 20, "normal"))

    def l_point(self):
        self.l_score += 1
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.update_scoreboard()

    # Printing winner of the game
    def game_over1(self):
        self.goto(0, 0)
        self.write("Player 2 is the winner of this game", align="center", font=("courier", 20, "normal"))

    def game_over2(self):
        self.goto(0, 0)
        self.write("Player 1 is the winner of this game", align="center", font=("courier", 20, "normal"))
