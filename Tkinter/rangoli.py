import turtle as t
t.bgcolor('black') #background color as black

t.pensize(2)
# screen setup
screen = t.Screen()
screen.setup(width = 1.0, height = 1.0)
t.speed(0)
col = ['red','cyan','magenta','blue','green','yellow','white']
for i in range(6):
    for colors in col:
        t.color(colors)
        t.circle(100)
        t.left(10)

t.hideturtle()
t.done()