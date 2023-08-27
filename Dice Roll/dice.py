import turtle
import random

def drawBox(x, y, size, color):
  turtle.color(color)
  turtle.setheading(0)
  turtle.up()
  turtle.goto(x, y)
  turtle.begin_fill()
  for x in range(4):
    turtle.forward(size)
    turtle.right(90)
  turtle.end_fill()

def rolls(x, y, size, radius, color, roll):
  turtle.color(color)
  turtle.up()

  #row 1
  turtle.goto(x+(size/6), y-(size/6)-radius)

  #circle 1
  if (roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6):
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

  turtle.forward(size/3)

  #circle 2
  '''
  if ():
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
  '''

  turtle.forward(size/3)

  #circle 3
  if (roll == 4 or roll == 5 or roll == 6):
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

  #row 2
  turtle.goto(x+(size/6), y-(size/6)-(size/3)-(radius))

  #circle 1
  if (roll == 6):
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

  turtle.forward(size/3)

  #circle 2
  if (roll == 1 or roll == 3 or roll == 5):
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

  turtle.forward(size/3)

  #circle 3
  if (roll == 6):
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

  #row 3
  turtle.goto(x+(size/6), y-(size/6)-((size/3)*2)-(radius))

  #circle 1
  if (roll == 4 or roll == 5 or roll == 6):
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

  turtle.forward(size/3)

  #circle 2
  '''
  if ():
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
  '''

  turtle.forward(size/3)

  #circle 3
  if (roll == 2 or roll == 3 or roll == 4 or roll == 5 or roll == 6):
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def Die(x, y, size, radius, color1, color2):
  turtle.speed(0)
  turtle.hideturtle()
  x -= (size/2)
  y += (size/2)
  drawBox(x, y, size, color1)
  rolls(x, y, size, radius, color2, random.randint(1, 6))
