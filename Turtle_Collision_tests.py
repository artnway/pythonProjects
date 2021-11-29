from random import randint, uniform, choice
import turtle as tu

tu.hideturtle()
number_of_turtles = 2
steps_of_time_number = 100000

def main():

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


main()


class Particle(tu.Turtle):
    default_distance = 0

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.shapesize(.5)
        self.object = tu.Turtle()


pool = [Particle() for i in range(number_of_turtles)]


pool[1].setpos(-50, 0)
pool[0].setpos(50, 0)
pool[1].setheading(0)
pool[0].setheading(0)
pool[0].setheading(180)
pool[0].default_distance = uniform(.01, .05)
pool[1].default_distance = uniform(.01, .05)


for i in range(steps_of_time_number):
    if pool[0].distance(pool[1]) < 1:
        pool[0].rt(180)
        pool[1].rt(180)
    for item in pool:
        item.forward(item.default_distance)
        x = 180 - item.heading()
        y = 360 - item.heading()
        if item.xcor() >= 98.5:
            item.seth(x)
        elif item.xcor() <= -98.5:
            item.seth(x)
        elif item.ycor() <= -98.5:
            item.seth(y)
        elif item.ycor() >= 98.5:
            item.seth(y)

    tu.update()

tu.done()
