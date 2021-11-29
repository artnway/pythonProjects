from random import randint
import turtle as tu


number_of_turtles = 30
steps_of_time_number = 10000
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
tu.hideturtle()
tu.tracer(0)


pool = {tu.Turtle(shape='circle') for i in range(number_of_turtles)}
for unit in pool:
    unit.shapesize(.5)
    unit.penup()
    unit.speed(0)
    unit.setpos(randint(-90, 90), randint(-90, 90))
    unit.setheading(randint(0, 360))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(.25)
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
