# Importing the randint module and Turtle class in order to create the Food class
from turtle import Turtle
from random import randint


class Food(Turtle):
    """ This class creates objects that function like the food the snake eats and moves randomly after being eaten"""
    def __init__(self):
        super().__init__()
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.shape("circle")
        self.x = 0
        self.y = 0
        self.move()

    def move(self):
        """ This function changes the position of the food to a random position on the screen"""
        self.x = randint(-350, 350)
        self.y = randint(-350, 350)
        self.goto(self.x, self.y)
