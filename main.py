from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard


game_status = True

screen = Screen()
screen.setup(height=600, width=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer()


snake = Snake()
food = Food()
scoreboard = Scoreboard()


def collision_with_food():
    if snake.head.distance(food) < 10:
        snake.extend()
        food.change_location()
        scoreboard.add_score()
    else:
        pass


def collision_with_tail():
    for seg in snake.segments[1:]:
        if snake.head.distance(seg) < 10:
            return True
    return False


screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.listen()

while game_status:
    screen.update()
    time.sleep(0.05)
    snake.move()
    collision_with_food()
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
    if collision_with_tail():
        scoreboard.reset()
        snake.reset()


screen.exitonclick()
