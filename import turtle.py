import turtle

t= turtle.Turtle()
s= turtle.Screen()
s.bgcolor("black")
t.speed(10)
turtle.tracer(1,0)
t.color("#D4D2D1")

for i in range(400):
    t.forward(i)
    t.left(125)
    t.forward(i)
