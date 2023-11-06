#Jeff Almaraz
#11/1/23


import turtle

# Create a turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle for drawing
artist = turtle.Turtle()
artist.speed(1)  # Set the drawing speed

# Draw a triangle
for _ in range(3):
    artist.forward(100)  # Length of each side
    artist.left(120)  # Turn left by 120 degrees

# Close the drawing window on click
screen.exitonclick()

