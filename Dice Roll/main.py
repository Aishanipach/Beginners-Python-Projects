import dice
import turtle

def reroll():
  turtle.clear()
  turtle.tracer(0, 0)
  dice.Die(0, 0, 100, 10, "black", "red")

  dice.Die(0, 150, 100, 10, "black", "red")

  dice.Die(0, -150, 100, 10, "black", "red")
  turtle.update()

reroll()

turtle.onkey(reroll, "space")

turtle.listen()
turtle.mainloop()
