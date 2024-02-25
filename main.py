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

def snake_move():
  if snake.direction == "up"
  y = snake.ycor()
  snake.sety(y + 20)

  if snake.direction == "down"
  y = snake.ycor()
  snake.sety(y - 20)

  if snake.direction == "left"
  x = snake.xcor()
  snake.setx(x - 20)

  if snake.direction == "right"
  x = snake.xcor()
  snake.setx(x + 20)

# keybord banding
screen.listen()
screen.onkeypress(snake_go_up, "up")
screen.onkeypress(snake_go_down, "down")
screen.onkeypress(snake_go_left, "left")
screen.onkeypress(snake_go_right, "right")

while True:
  screen.update
  
  # snake & fruit colition
  if snake.distance(fruit) < 20:
    x = random.randing(-290, 270)
    y = random.randing(-240, 240)
    fruit.goto(x, y)
    scoring.clear
    score += 1
    scoring.write("score: {}".format(score),  align="center", font=("courier", 24, "bold"))
    delay -= 0.001

    # creating new foods
    new_fruit = turtle.Turtle()
    new_fruit.speed()
    new_fruit.shape("square")
    new_fruit.color("red")
    new_fruit.penup()
    old_fruit.append(new_fruit)
    
# adding ball to snake
for index in range(len(old_fruit), -1, 0, -1):
  a = old_fruit[index, -1].xcor()
  a = old_fruit[index, -1].ycor()
  
  old_fruit[index].goto(a, b)

if len(old_fruit) > 0:
  a = snake.xcor()
  b = snake.ycor()
  old_fruit[0].goto(a, b)

snake.move()

# snake border & colition
if snake.xcor() > 200 or snake.xcor() < -300 or snake.xcor() > 240 or snake.xcor() < -240:
  time.sleep()
  screen.clear()
  screen.bgcolor("turquoise")
  screen.goto(0, 0)
  screen.write(" Game Over /n Your score is {}".format(scrore), align="center", font=("courier", 30, "bold"))
  

