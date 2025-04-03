from turtle import *
import time
from food import Food
from scoreboard import ScoreBoard
from snake import Snake

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # enables code to happen without showing on screen

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

while True:
    screen.update() # updates screen hidden by tracer method
    time.sleep(0.1) # delays by 0.1 second
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15: #check distance between food and snake
        food.refresh()
        snake.extend()
        scoreboard.inc_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset_scoreboard()
        snake.reset_scoreboard()

    # Detect collision with tail
    for segment in snake.segments[1:]: # Python slicing ie returns the list from element 1 to the end
        if snake.head.distance(segment) < 10:
            scoreboard.reset_scoreboard()
            snake.reset_scoreboard()

