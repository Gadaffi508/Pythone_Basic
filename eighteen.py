#from turtle import Turtle , Screen

#timmy_the_turtle = Turtle()

#Turtle Properties
#timmy_the_turtle.shape("turtle")
#timmy_the_turtle.color("blue")
#timmy_the_turtle.forward(100)
#timmy_the_turtle.right(90)

#for _ in range(4):
#    timmy_the_turtle.forward(100)
#    timmy_the_turtle.left(90)

#screen = Screen()
#screen.exitonclick()

import turtle as t
import random

tim = t.Turtle()

# for _ in range(15):
    #tim.forward(10)
    #tim.penup()
    #tim.forward(10)
    #tim.pendown()

color=["CornflowerBlue","MidnightBlue","GreenYellow","AliceBlue","Lime","SkyBlue","DarkOrange"]

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

directions = [0,90,180,270]
tim.pensize(5)
tim.speed("fastest")

for _ in range(200):
    tim.color(random.choice(color))
    tim.forward(30)
    tim.setheading(random.choice(directions))

# for shape_slide_n in range(3,11):
    #tim.color(random.choice(color))
    #draw_shape(shape_slide_n)