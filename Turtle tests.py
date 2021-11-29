from random import randint, uniform, choice
import turtle as tu

tu.hideturtle()
number_of_turtles = 10
steps_of_time_number = 10000

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


def draw_pool():
    for item in pool:
        item.speed(1)
        item.setpos(randint(-90, 90), randint(-90, 90))
        item.setheading(randint(0, 360))
        item.default_distance = uniform(.05, .1)


draw_pool()

for i in range(steps_of_time_number):
    for item in pool:
        for b in pool:
            x = 180 - item.heading()
            y = 360 - item.heading()
            a = item.distance(item) + item.distance(b)
            if 0 < a < 5:
                print(a)
                l = item.heading()
                z = b.heading()
                item.setheading(z)
                b.setheading(l)
                item.default_distance += .1
                b.default_distance -= .1
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
