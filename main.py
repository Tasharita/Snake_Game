from turtle import *
import time

from snake import Snake

screen = Screen()
screen.setup(width = 600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0) # enables code to happen without showing on screen

snake = Snake()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    screen.update() # updates screen hidden by tracer method
    time.sleep(1) # delays by 1 second

    snake.move()

screen.exitonclick()