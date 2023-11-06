#jeff Almaraz
#11/1/23

#program that asks the user for number of sides the legnth of the side, and thge color of the line, fill color

import turtle
# Function to draw a regular polygon
def draw_regular_polygon(side,length,line_color,fill_color):
    turtle.pencolor(line_color)
    turtle.fillcolor(fill_color)
    turtle.begin_fill()

    for _ in range(sides):
        turtle.forward(length)
        turtle.left(360 / sides)

    turtle.end_fill()

# Input from the user
sides = int(input("enter the number of sides for the polygon: "))
Length = float(input("Enter the length of each side: "))
line_color = input("enter the color of the polygon's outline: ")
fill_color = input ("enter the fill color of the polygon: ")

# Initialize the Turtle graphics window
turtle.speed(1)
turtle.bgcolor("white")

# Draw and fill the regular polygon
draw_regular_polygon(sides, Length, line_color, fill_color)

# Close the graphics window when clicked
turtle.exitonclick()


