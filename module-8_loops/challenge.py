import turtle

# create a sketch program
pen_color = input("Enter a pen color : ")
line_length = int(input("Enter a line length : "))
angle = int(input("Angle : "))
count = 0

if line_length <= 0:
    raise ValueError("line length must be line_length > 0")

turtle.color(pen_color)

while count < 4:
    turtle.forward(line_length)
    turtle.right(angle)
    count += 1

turtle.done()
