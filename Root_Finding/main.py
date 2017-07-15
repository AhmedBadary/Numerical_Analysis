# Author: Ahmad Thabet Mohammad Badary
# Date: Jun 30 2017

import find_bracket as fb
import newton_bisection as nb
import math as m
import helper_functions as hf
def f(x):
    return m.cos(x) - (x * m.exp(-x))

def df(x):
    return m.exp(-x)*(x - m.exp(x)*m.sin(x) - 1)

a = 1.9
b = 30
tol = 10**-9
dx = 10**-10
x_vals = [i - 3 for i in range(14)]

# Testing the FINDBRACKET Function
def test_findbracket():
    def f(x):
        return 2*x**2-3*x-5
    print("Testing Function: FINDBRACKET()")
    print("Running 8 Tests")
    x0_vals = [i-4 for i in range(8)]
    dx = 10**-10
    success = True
    for x0 in x0_vals:
        a, b = fb.find_bracket(f, x0, dx)
        if hf.sgn(f(a)) * hf.sgn(f(b)) > 0:
            success = False
    if success:
        print("All tests Successful")
    else:
        print("At least one Test Cases Failed")

# Testing the NEWTONBISECTION Function
def test_newtonbisection():
    def f(x):
        return 2*x**2-3*x-5
    def df1(x):
        return 4*x-3

    print("Testing Function: NEWTONBISECTION()")
    print("Running 5 Tests")
    a_b = [[-2, 0.5], [-3,0], [0, 3], [-0.5, 5], [1, 4]]
    tol = 10**-9
    success = True
    for els in a_b:
        a = els[0]
        b = els[1]
        p = nb.newton_bisection(f, df, a, b, tol)
        if f(p) > tol:
            success = False
    if success:
        print("All tests Successful")
    else:
        print("At least one Test Cases Failed")

# Implements PART 3
def Pr_3():
    arg = nb.newton_bisection_tt(f, df, a, b, tol)
    print("Format: Iteration, Method, a, b, p, f(p)\n")
    write(arg, "Problem 3: \n", 'w')
    print("Successfully written results to \"results.csv\" \nProblem 3 Completed!")


# Implements PART 4
def Pr_4():
    arg = []
    for x0 in x_vals:
        in_arg = [x0]
        a, b = fb.find_bracket(f, x0, dx)
        x = nb.newton_bisection(f, df, a, b, tol)
        in_arg.extend([a, b, x])
        arg.append(in_arg)

    print("Format: x0, a, b, x \n")
    write(arg, "Problem 4: \n", 'a')
    print("Successfully written results to \"results.csv\" \nProblem 4 Completed!")


# Writes Results to File
def write(arg, problem, method, _f="results.csv"):
    f = open(_f, method)
    if method == 'w':
        f.write("# Author: Ahmad Thabet Mohammad Badary\n# Date: Jun 30 2017\n\n")
        f.write(problem)
        f.write(" | Iter # | Method    |        a          |        "+
            "b          |        p          |       f(p)             |\n")
        f.write(" |--------+-----------+-------------------+-----"+
            "--------------+-------------------+------------------------|\n")
        for el in arg:
            f.write(" |   ")
            for elem in el:
                elem = fix_elem(elem, el[0], el[1], el[-1])
                if elem == el[0]:
                    if elem < 10:
                        f.write(' ' + str(elem) + "   | ")
                    else:
                        f.write(str(elem) + "   | ")
                else:
                    if elem == el[-1]:
                        elem = str(elem)
                        if len(elem) < 23:
                            for i in range(23 - len(str(elem))):
                                elem += ' '
                        f.write(elem + '|\n')    
                    else:
                        f.write(str(elem) + ' | ')
        f.write('\n \n \n \n \n')

    else:
        f.write(problem)
        f.write(" |   x0     |            a              |             "+
            "b             |            x         |\n")
        f.write(" |----------+---------------------------+-------"+
            "--------------------+----------------------|\n")
        for el in arg:
            f.write(" |   ")
            for elem in el:
                if elem == el[0] and elem < 10 and elem >= 0:
                    f.write(' ')
                if elem == el[-1]:
                    elem = fix_elem(elem, el[0], -9999999, -9999999)
                    f.write(str(elem) + '|\n')
                else:
                    elem = fix_elem(elem, el[0], -9999999, -9999999)
                    f.write(str(elem) + '     |     ')
  
# Helper Function for the Formatting of the table
def fix_elem(elem, el0, el1, el5):
    if elem != el0 and elem != el1 and elem != el5: 
        if len(str(elem)) < 18:
            elem = str(elem)
            for i in range(17 - len(str(elem))):
                elem += "0"
        else:
            elem = str(elem)
            for i in range(len(str(elem))-17):
                elem = elem[:-1]
    return elem


# Run this to run all the code in this File
def master():
    print("\nRunning Tests \n")
    test_findbracket()
    print("------------------------------------------------ \n")
    test_newtonbisection()
    print("________________________________________________ \n")

    print("Running Part 3:\n Run newton_bisection with the function\n",
    "f(x) = cos(x)−x*exp(−x) on the interval [1.9,30] with ε = 10^(−9). \n")
    Pr_3()


    print("________________________________________________ \n")

    print("Running Part 4:\n Combine the functionality of find_bracket with \n",
        "newton_bisection in order to solve for the \n roots  of f(x) = cos(x)−xexp(−x)  with",
        "x0 = −3,−2,−1, . . . ,10 \n")
    Pr_4()

    print("________________________________________________ \n")

    print("All test cases completed! \nAll methods executed and results saved!")

master()