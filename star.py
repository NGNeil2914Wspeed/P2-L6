import turtle

turtle.Screen().bgcolor("green")
turtle.Screen().setup(670, 670)

lookatthestars = turtle.Turtle()

lookatthestars.forward(100)

def lookna():

    for _ in range(2):
        lookatthestars.left(120)
        lookatthestars.forward(100)

lookna()

lookatthestars.penup()

lookatthestars.right(100)
lookatthestars.forward(90)
lookatthestars.pendown()
lookna()
turtle.done()