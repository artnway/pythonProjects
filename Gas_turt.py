from random import randint
import turtle as tu

number_of_turtles = 30
steps_of_time_number = 10


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
pool = [tu.Turtle() for x in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(1)
    unit.goto(randint(-50, 50), randint(-50,50))



for pool[1] in range(steps_of_time_number):
    movement()
for pool[2] in range(steps_of_time_number):
    movement()

tu.done()
