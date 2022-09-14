from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Sets various display settings.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

# Calls the Snake class which initializes the first 3 segments of the snake and calls food which creates a food.
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Allows control of the snake using arrow keys.
screen.listen()
screen.onkey(snake.move_up, 'Up')
screen.onkey(snake.move_down, 'Down')
screen.onkey(snake.move_left, 'Left')
screen.onkey(snake.move_right, 'Right')

# Updates the screen after moving all the segments, delays the segment movement, and continuously moves until game over.

game_over = False
while not game_over:
    screen.update()
    time.sleep(0.09)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_over = True
        scoreboard.game_over()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_over = True
            scoreboard.game_over()

screen.exitonclick()
