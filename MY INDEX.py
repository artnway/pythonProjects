import turtle as tu
import numpy as np

tu.shape('turtle')
tu.pencolor("darkblue")
tu.pensize(2)
tu.speed(4)
tu.penup()
tu.pendown()

index = list(input("Введи ваш индекс: "))
index = [int(item) for item in index]
st2 = 25
st = 25
dig = np.sqrt(st ** 2 + st ** 2)


def prints(i):
    if i == 0:
        zero()

    elif i == 1:
        one()

    elif i == 2:
        two()

    elif i == 3:
        three()

    elif i == 4:
        four()

    elif i == 5:
        five()

    elif i == 6:
        six()

    elif i == 7:
        seven()

    elif i == 8:
        eight()

    else:
        i = 9
        nine()


def zero():
    tu.fd(st)
    tu.rt(90)
    tu.fd(st * 2)
    tu.rt(90)
    tu.fd(st)
    tu.rt(90)
    tu.fd(st * 2)


def one():
    tu.rt(90)
    tu.penup()
    tu.fd(st)
    tu.pendown()
    tu.lt(135)
    tu.fd(dig)
    tu.rt(135)
    tu.fd(st * 2)


def two():
    tu.fd(st)
    tu.rt(90)
    tu.fd(st)
    tu.rt(45)
    tu.fd(dig)
    tu.lt(135)
    tu.fd(st)


def three():
    tu.fd(st)
    tu.rt(135)
    tu.fd(dig)
    tu.lt(135)
    tu.fd(st)
    tu.rt(135)
    tu.fd(dig)


def four():
    tu.rt(90)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.rt(180)
    tu.fd(st * 2)


def five():
    tu.penup()
    tu.fd(st)
    tu.rt(180)
    tu.pendown()
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.rt(90)
    tu.fd(st)
    tu.rt(90)
    tu.fd(st)


def six():
    tu.penup()
    tu.fd(st)
    tu.rt(135)
    tu.pendown()
    tu.fd(dig)
    tu.lt(45)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)


def seven():
    tu.fd(st)
    tu.rt(135)
    tu.fd(dig)
    tu.lt(45)
    tu.fd(st)


def eight():
    tu.fd(st)
    tu.rt(90)
    tu.fd(st)
    tu.rt(90)
    tu.fd(st)
    tu.rt(90)
    tu.fd(st)
    tu.rt(180)
    tu.fd(st * 2)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)


def nine():
    tu.rt(90)
    tu.penup()
    tu.fd(st * 2)
    tu.pendown()
    tu.lt(135)
    tu.fd(dig)
    tu.lt(45)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)
    tu.fd(st)
    tu.lt(90)


tu.penup()
tu.fd(st2)
tu.pendown()
for i in index:
    prints(i)
    tu.penup()
    tu.home()
    st2 = st2 + 50
    tu.fd(st2)
    tu.pendown()

tu.done()
