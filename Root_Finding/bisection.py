# Author: Ahmad Thabet Mohammad Badary
# Date: Jun 30 2017

import numpy as np
import math as m
import time
import helper_functions as hf

# Bisection Method
""" BISECTION ()
* An implementation of the Bisection Method.
"""
def bisection(f, a, b, tol):
    iters = 0
    st = time.clock()

    while (iters < 2000):
        p = (a+b) * 0.5
        iters += 1
        if (p-a) < tol:
            break
        if sgn(f(a)) * sgn(f(p)) > 0:
            a = p
        else:
            b = p

    if iters >= 200:
        print("Max-Iteration Reached!")
    else:
        print("Iterations = ", iters)
    ed = time.clock()
    iters += 1
    print("Time: ", int((-st + ed)//60), "m + ", (((-st + ed)/60)%1)*60, "s")
    return p
