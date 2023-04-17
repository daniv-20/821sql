"""Docstring."""
import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create the turtle
turnip = turtle.Turtle()
turnip.color("purple", "green")
turnip.pensize(3)
turnip.speed(0)

# Draw the turnip shape
turnip.begin_fill()
turnip.circle(50)
turnip.circle(30, 180)
turnip.circle(80, 180)
turnip.circle(30, 180)
turnip.circle(50)
turnip.end_fill()

# Draw the turnip's leaves
turnip.penup()
turnip.goto(-70, 70)
turnip.pendown()
turnip.begin_fill()
turnip.setheading(40)
turnip.circle(30, 120)
turnip.setheading(220)
turnip.circle(-30, 120)
turnip.end_fill()

# Hide the turtle and exit the screen on click
turnip.hideturtle()
screen.exitonclick()
