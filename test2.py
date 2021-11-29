import turtle as tur
import numpy as np

tur.shape('turtle')
tur.speed(10)
fib1 = fib2 = 1
k = 2 * np.pi
n = 1

for t in range(20):
    fib1, fib2 = fib2, fib1 + fib2
    b=t*k
    tur.fd(fib2)
    tur.lt(b)
tur.done()