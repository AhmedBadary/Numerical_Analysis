# Author: Ahmad Thabet Mohammad Badary
# Date: Jun 30 2017

import numpy as np
import math as m
import time as t
import helper_functions as hf

""" NEWTON BISECTION To Table ()
* An implementation of a function that finds root by repeated application
  of two methods, Newton's Method and the Bisection Method.
* The function chooses which method to apply at every step.
* Returns a root of function "F" in the intervel "[A, B]", with accuracy < TOL.
"""
def newton_bisection(f, df, a, b, tol):
    assert (hf.sgn(f(a)) * hf.sgn(f(b)) == -1)
    iters = 0

    st = t.clock()
    p = a
    while (m.fabs(f(p)) > tol and iters < 200):
        p = p - f(p)/df(p)
        iters += 1
        if not (p >= a and p <= b):
            p = 0.5 * (a+b)
        if hf.sgn(f(a)) * hf.sgn(f(p)) < 0:   
            b = p 
        else:
            a = p
    # !!! (Un)comment the next FOUR line to: INFORM IF MAX ITERATIN NUMBER REACHED !!!
    # if iters >= 200:
    #     print("Max-Iteration Reached!")
    # else:
    #     print("Iterations = ", iters)
    ed = t.clock()
    # !!! (Un)comment the next line to: DISPLAY THE TIME LAPSED !!!
    # print("Time: ", int((-st + ed)//60), "m + ", (((-st + ed)/60)%1)*60, "s")
    return p


""" NEWTON BISECTION To Table ()
* An implementation of a function that finds root by repeated application
  of two methods, Newton's Method and the Bisection Method.
* The function chooses which method to apply at every step.
* Returns a root of function "F" in the intervel "[A, B]", with accuracy < TOL.

* This is a modified function of the NEWTON_BISECTION Function that supports
  printing the results in a table.
"""
def newton_bisection_tt(f, df, a, b, tol):
    assert (hf.sgn(f(a)) * hf.sgn(f(b)) == -1)
    iters = 0
    to_print = []

    p = a
    while (m.fabs(f(p)) > tol and iters < 200):
        to_add_to_print = []
        to_add_to_print.append(iters)
        p = p - f(p)/df(p)

        if not (p >= a and p <= b):
            p = 0.5 * (a+b)
            to_add_to_print.append("Bisection")
            if hf.sgn(f(a)) * hf.sgn(f(p)) < 0:   
                b = p 
            else:
                a = p
            to_add_to_print.extend([a, b, p, f(p)])
        else:
            to_add_to_print.append("Newton   ")
            if hf.sgn(f(a)) * hf.sgn(f(p)) < 0:   
                b = p 
            else:
                a = p
            to_add_to_print.extend([a, b, p, f(p)])
        iters += 1
        to_print.append(to_add_to_print)

    return to_print
