# Importing the time module, Snake, Screen, Food and Score class in order to create the snake game
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Creating the screen object from the Screen class and setting its width and height to 800
screen = Screen()
screen.setup(800, 800)
# Using the tracer function to reduce the lag
screen.tracer(0)
screen.title("Ope's Snake game")

# Creating the snake, food and score objects from their various classes
snake = Snake()
food = Food()
score = Score()

# Defining the parameter game_on that allows the game to continually play until game over
game_on = True

# Using the listen function to allow for the game to take key inputs and also defining does inputs and their functions
screen.listen()
screen.onkey(snake.snake_up, "Up")
screen.onkey(snake.snake_down, "Down")
screen.onkey(snake.snake_right, "Right")
screen.onkey(snake.snake_left, "Left")

# Using the while loop to loop around the game program to allow the game to play continuously
while game_on:
    # Using the time.sleep function to slow down the speed of the program so as to make the game playable
    time.sleep(0.1)
    # Works in hand with the tracer function
    screen.update()
    # Using the score.writing function to write the score at the top of the screen
    score.writing()

    # Using the if statement to determine when the food has been eaten and adding a segment to the snake
    # and a point to the score when it has as well as making the food move to a random location on the screen
    if food.distance(snake.head) < 15:
        food.move()
        snake.add_segment()
        score.score += 1

    # Using the if statement to determine if the snake has left the boundary and the initializing the game over
    if snake.head.xcor() > 390 or snake.head.xcor() < -390:
        score.highscore()
        snake.reset()
        score.game_over()
        game_on = False
    if snake.head.ycor() > 390 or snake.head.ycor() < -390:
        score.highscore()
        snake.reset()
        score.game_over()
        game_on = False

    # Using the if statement to determine if the snake has eaten its tail and the initializing the game over
    for segment in snake.segments[3:]:
        if snake.head.distance(segment) < 10:
            score.highscore()
            snake.reset()
            score.game_over()
            game_on = False

    # This function causes the sake to move in the direction its head is facing continuously
    snake.snake_walk()

# This function allows the screen to stay on until the game has come to an end
screen.exitonclick()
