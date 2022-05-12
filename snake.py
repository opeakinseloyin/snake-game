# Importing the Turtle class in order to create the Snake class
from turtle import Turtle


class Snake:
    """ This class creates objects that function and act like the snake used in the game"""
    def __init__(self):
        self.segments = []
        self.x = 0
        self.y = 0
        self.create_snake()
        self.head = self.segments[0]
        self.length = len(self.segments) - 1

    def create_snake(self):
        # Using the for loop to create the different segments of the snake
        for segment in range(3):
            segment = Turtle()
            segment.shape("square")
            segment.penup()
            segment.goto(self.x, self.y)
            self.x += 20
            self.segments.append(segment)
            segment.xcor()

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
        self.length = len(self.segments) - 1

    def snake_walk(self):
        """ This function moves the snake forward by 20 paces"""
        for seg_num in range(self.length, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)

    def snake_up(self):
        """ This function changes the direction of the snake up(90 degrees)"""
        # Using the if statement to stop the user from going the opposite direction immediately
        if self.head.heading() != 270:
            self.head.setheading(90)

    def snake_down(self):
        """ This function changes the direction of the snake down(270 degrees)"""
        # Using the if statement to stop the user from going the opposite direction immediately
        if self.head.heading() != 90:
            self.head.setheading(270)

    def snake_right(self):
        """ This function changes the direction of the snake right(0 degrees)"""
        # Using the if statement to stop the user from going the opposite direction immediately
        if self.head.heading() != 180:
            self.head.setheading(0)

    def snake_left(self):
        """ This function changes the direction of the snake left(180 degrees)"""
        # Using the if statement to stop the user from going the opposite direction immediately
        if self.head.heading() != 0:
            self.head.setheading(180)

    def add_segment(self):
        """ This function adds an extra segment to the snake"""
        new_segment = Turtle("square")
        new_segment.penup()
        self.segments.append(new_segment)
        self.length = len(self.segments) - 1
