# Author: Ahmad Thabet Mohammad Badary
# Date: Jun 30 2017

import numpy as np
import math as m
import time
import helper_functions as hf

""" NEWTON ()
* An implementation of Newton's Method.
"""
def newton(f, df, p0, tol):
    iters = 0
    st = time.clock()

    while (iters < 200):
        p = p0 - f(p0)/df(p0)
        iters += 1
        if m.fabs(p-p0) < tol:
            continue
        p0 = p
    if iters >= 200:
        print("Max-Iteration Reached!")
    else:
        print("Iterations = ", iters)
    ed = time.clock()
    iters += 1
    print("Time: ", int((-st + ed)//60), "m + ", (((-st + ed)/60)%1)*60, "s")
    return p