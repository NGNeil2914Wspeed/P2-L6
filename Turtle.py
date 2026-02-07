import turtle

t = turtle.Turtle()
t.speed(5)

for _ in range(4):
    t.forward(100)   # side length
    t.right(90)      # 90° turn for a square

turtle.done()
