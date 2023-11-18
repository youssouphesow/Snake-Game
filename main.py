#Snake Game
#import packages

import turtle
import random
import time

# Create screen
screen = turtle.screen()
screen.title("Snake Game")
screen.setup(width=700, height=700)
screen.tracer(0)
screen.bgcolor("1d1d1d")

# Create border
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310, 250)
turtle.pendown()
turtle.color("red")
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.penup()
turtle.hideturtle()

#score 
score = 0
delay = 0.1

#snake
snake = turtle.Turtle()
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"

#food
fruit = turtle.Turtle()
fruit.speed()
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# scoring
scoring = turtle.Turtle()
scoring.speed()
scoring.color(""white)
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("score : ", align="center", font=("courier", 24, "bold"))

# definie how to move
def snake_go_up():
  if snake.direction != "down":
    snake.direction = "up"

def snake_go_down():
  if snake.direction != "up":
    snake.direction = "down"

def snake_go_left():
  if snake.direction != "right":
    snake.direction = "left"

def snake_go_right():
  if snake.direction != "left":
    snake.direction = "right"

def snake_move:
