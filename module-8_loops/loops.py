import turtle

turtle.bgcolor("black")
turtle.color("red")

n = 6
for steps in range(n):
    turtle.forward(10)
    turtle.right(360/n)
    for j in range(n):
        turtle.forward(50)
        turtle.right(360/n)

turtle.done()
