# Author: Ahmad Thabet Mohammad Badary
# Date: Jun 30 2017

import numpy as np
import math as m
import time
import helper_functions as hf

# Fixed Point Iteration
""" Fixed_Pt_Iter ()
* An implementation of the Bisection Method.
"""
def fixed_pt_iter(f, p0, tol):
    p = f(p0)
    while 1:
        p = f(p0)
        if abs(p - p0) < tol:
            return p
        print(p)
        p0 = p