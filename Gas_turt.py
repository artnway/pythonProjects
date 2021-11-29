from random import randint
import turtle as tu

number_of_turtles = 500
steps_of_time_number = 10



class Pool(turtle.Turtle):
    def __init__(self, color, distance, shape):
        super().__init__()
        self.object = turtle.Turtle()
        self.penup()
        self.forward(distance)
        self.color = color
        self.shape = shape
        self.pendown()
        self.color = 'black'
        self.shape = 'circle'




def ready():
    tu.shape('circle')
    tu.shapesize(.5)
    tu.setworldcoordinates(-100, -100, 100, 100)
    tu.speed(0)
    tu.pensize(3)
    tu.penup()
    tu.goto(-100, 100)
    tu.pendown()
    tu.goto(100, 100)
    for i in range(3):
        tu.rt(90)
        tu.fd(200)
    tu.penup()
    tu.home()


def movement():
    unit.shape('circle')
    unit.shapesize(0.5)
    unit.forward(1.5)
    x = 180 - unit.heading()
    y = 360 - unit.heading()
    if unit.xcor() >= 98.5:
        unit.seth(x)
    elif unit.xcor() <= -98.5:
        unit.seth(x)
    elif unit.ycor() <= -98.5:
        unit.seth(y)
    elif unit.ycor() >= 98.5:
        unit.seth(y)
    tu.update()

ready()
tu.tracer(0)
pool = [Pool for x in range(number_of_turtles)]



for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(1)
        x = 180 - unit.heading()
        y = 360 - unit.heading()
        if unit.xcor() >= 98.5:
            unit.seth(x)
        elif unit.xcor() <= -98.5:
            unit.seth(x)
        elif unit.ycor() <= -98.5:
            unit.seth(y)
        elif unit.ycor() >= 98.5:
            unit.seth(y)

        tu.update()

tu.done()
