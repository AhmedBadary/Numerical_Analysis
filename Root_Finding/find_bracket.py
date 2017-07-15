# Author: Ahmad Thabet Mohammad Badary
# Date: Jun 30 2017

import numpy as np
import math as m
import time
import helper_functions as hf


""" FIND BRACKET ()
This function return an interval, where at the left endpoint the function has
a NEGATIVE value and on the right endpoint has a POSITIVE value.
This is to invoke the Intermediate Value Theorem. 
It ensures the existance of a root within the interval.
"""
def find_bracket(f, x0, dx):
    a = b = x0
    while 1:
        a -= dx
        if hf.sgn(f(a)) * hf.sgn(f(b)) < 0:
            return a, b
        b += dx
        if hf.sgn(f(a)) * hf.sgn(f(b)) < 0:
            return a, b
        dx *= 2