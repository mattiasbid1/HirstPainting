from turtle import Turtle, Screen
import random


def color():
    return (random.random(), random.random(), random.random())

def dot_painter(x, y):
    timmy.penup()
    timmy.setposition(-180, -180)
    for i in range(x):

        for j in range(y):
            timmy.dot(20, color())
            timmy.forward(50)

        timmy.setposition(-180, (-180 + 50 * (i+1)))



timmy = Turtle()
screen = Screen()

timmy.speed(0)
timmy.hideturtle()

dot_painter(10, 10)

screen.exitonclick()
