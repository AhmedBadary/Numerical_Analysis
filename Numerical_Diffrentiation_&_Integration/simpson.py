import math as m, numpy as np
def simpson(f, a, b, n):
    h = (b-a) / n
    k = 0
    x = a + h
    for i in range(1, int(n/2 + 1)):
        k += 4*f(x)
        x += 2*h
    x = a + 2*h
    for i in range(1,int(n/2)):
        k += 2*f(x)
        x += 2*h
    return (h/3)*(f(a)+f(b)+k)
n = 2

def f(x):
    # return 2 / (x**2 - 4)
    return x**2 * m.sin(x)
# a, b =  0, 0.35
a, b =  0, m.pi/4

print(simpson(f, a, b, n))