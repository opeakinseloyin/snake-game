# Importing the Turtle class in order to create the Score class
from turtle import Turtle


class Score(Turtle):
    """ This class creates objects that write the score of the player at the top of the screen"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 350)
        with open("data.txt") as file:
            content = file.read()
        self.high_score = int(content)
        self.score = 0
        self.write(arg=f"Score: {self.score}", align="center", font=("Courier", 14, "normal"))

    def writing(self):
        """ This function updates the score writing at the top of the screen"""
        self.clear()
        self.write(arg=f"Score: {self.score}. High score: {self.high_score}", align="center", font=("Courier", 14, "normal"))

    def add_score(self):
        """ This function increases the score of the player"""
        self.score += 1

    def game_over(self):
        """ This function writes game over in the middle of the screen"""
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=("Courier", 18, "normal"))

    def highscore(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(f"{self.score}")
            self.high_score = self.score
        self.score = 0
