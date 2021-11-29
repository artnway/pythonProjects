import turtle as tu

tu.shape("turtle")
tu.color('darkred')
tu.penup()
tu.speed(0)
tu.setpos(300, 50)
tu.pendown()
tu.lt(0)


def butter(n):
    an = 90 / n
    for n in range(n):
        tu.circle(150)
        tu.lt(an)
    tu.penup()
    tu.setpos(0, 50)
    tu.pendown()
    an = 90 / n
    for n in range(n*2):
        tu.circle(-150)
        tu.rt(an)
    tu.penup()
    tu.setpos(-300, 50)
    tu.pendown()
    n=32
    an = 90 / n
    for n in range(n):
        tu.circle(150)
        tu.lt(an)


butter(32)
tu.done()
