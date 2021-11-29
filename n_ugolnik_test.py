import turtle as tu
import numpy as np


tu.shape("turtle")
tu.color('darkred')
tu.speed(6)


def angle(n, b):
    for n in range(4, n):
        z = 180 * (n - 2) / n / 2
        tu.lt(z)
        ots = 48 / (2 * np.sin(np.radians(180/n)))
        print(ots)
        for i in range(n):
            an = 360 / n
            tu.lt(an)
            tu.fd(b+ots/2)
        tu.penup()
        tu.rt(z)
        tu.fd(ots/4)
        tu.pendown()
        print(b)

angle(20, 30)

tu.done()
