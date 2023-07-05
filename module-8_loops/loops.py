import turtle

turtle.bgcolor("white")

my_list = ['red', 'green', 'blue', 'orange']
for steps in range(0, len(my_list)):
    turtle.color(my_list[steps])
    turtle.forward(10)
    turtle.right(360/len(my_list))
    for j in range(len(my_list)):
        turtle.forward(50)
        turtle.right(360/len(my_list))

turtle.done()
