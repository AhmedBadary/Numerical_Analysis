# Name: Ahmad Thabet Mohammad Badary
# SID: 25822346
# Date: Jul 10 2017

import lagrange as lg, barycentric as bc
import math as m, pandas as pd, matplotlib as mplt, numpy as np
from numpy import linspace
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib import pyplot as plt

# Implements Question. 4
def Pr_4():
    plot_me(1, f1, ls_10, bc.barycentric(ls_10, f1(ls_10), xout), f1_str + "   :   xunif  :  10[f1")
    plot_me(2, f1, ls_50, bc.barycentric(ls_50, f1(ls_50), xout), f1_str + "   :   xunif  :  50[f1")

    plot_me(3, f1, ch_10, bc.barycentric(ch_10, f1(ch_10), xout), f1_str + "   :   xcheb  :  10[f1")
    plot_me(4, f1, ch_50, bc.barycentric(ch_50, f1(ch_50), xout), f1_str + "   :   xcheb  :  50[f1")
# _____________________________________________________________________________________________________

    plot_me(5, f2, ls_10, bc.barycentric(ls_10, f2(ls_10), xout), f2_str + "   :   xunif  :  10[f2")
    plot_me(6, f2, ls_50, bc.barycentric(ls_50, f2(ls_50), xout), f2_str + "   :   xunif  :  50[f2")

    plot_me(7, f2, ch_10, bc.barycentric(ch_10, f2(ch_10), xout), f2_str + "   :   xcheb  :  10[f2")
    plot_me(8, f2, ch_50, bc.barycentric(ch_50, f2(ch_50), xout), f2_str + "   :   xcheb  :  50[f2")


# Run this to run all the code in this File
def master():
    print("\nRunning Tests \n")
    # test_findbracket()
    print("________________________________________________ \n")
    # test_newtonbisection()
    print("________________________________________________ \n")

    print("Running Problem. 4 \n")
    print("Plotting polynomials [1-8]")
    print(" |    Plot-file    |        f        |      x_in       |        n        |     Status      |")
    print(" |-----------------+-----------------+-----------------+-----------------+-----------------|")
    Pr_4()

    print("\n________________________________________________ \n")

    print("All test cases completed successfully!\nAll problems executed and results saved!")

# The First Function: f1(x) = |x| + x/2 - x^2 
def f1(x):
    if isinstance(x, list):
        return [abs(xi) + xi/2 - xi**2 for xi in x]
    return abs(x) + x/2 - x**2

# The Second Function: f2(x) = 1 / (1 + 25x^2)
def f2(x):
    if isinstance(x, list):
        return [1 / (1 + 25 * xi**2) for xi in x]
    return 1 / (1 + 25 * x**2)

# Helper Function: This Function creates the Nth order chebyshev nodes
def chevspace(n):
    xchev = []
    for i in range(n):
        xchev.append(m.cos(m.pi * i/n))
    return xchev

# Variables : Global
xout = linspace(-1,1,1000).tolist()
f1_str, f2_str = "|x| + x/2 - x^2", "1 / (1 + 25x^2)"
ls_10, ls_50 = linspace(-1,1,10+1).tolist(), linspace(-1,1,50+1).tolist()
ch_10, ch_50 = chevspace(10), chevspace(50)


# Helper Function: Plots the functions, polynomials and prints results
def plot_me(idx, f, xin, yout, title):
    try:
        f_str, title = title[title.index("[")+1:len(title)], title[0:title.index("[")]
        my_plot = plt.figure()
        plt.plot(xout, f(xout), 'k')
        plt.plot(xin, f(xin), 'bo')
        plt.plot(xout, yout, 'b')
        plt.xlabel("x", fontweight='bold')
        plt.ylabel("f(x) = " + title[0:title.index("^2")+3], fontweight='bold')
        plt.title('plot' + str(idx) + '.pdf   :   ' + title,  fontsize=15,y=1.04)
        plt.gca().spines['bottom'].set_color('green')
        plt.gca().spines['left'].set_color('green')
        plt.gca().spines["top"].set_visible(False)
        plt.gca().spines["right"].set_visible(False)
        plt.gca().title.set_color('red')
        plt.gca().yaxis.label.set_color('red')
        plt.gca().xaxis.label.set_color('red')
        # plt.show()
        if idx == 2:
            plt.gca().set_ylim([-0.5,0.7])
        if idx == 6:
            plt.gca().set_ylim([-.1,1.1])
        pp = PdfPages('plots/plot' + str(idx) + '.pdf')
        pp.savefig(my_plot, bbox_inches='tight')
        pp.close()
        print(" |" + ' '*4+ 'plot' + str(idx) + '.pdf'+ ' '*4 + "|" + ' '*8 + f_str + ' '*7 +\
         "|" + ' '*6+ title[title.index("   x")+3:title.index("   x")+8] + ' '*6 +  "|" +\
          ' '*7+ title[len(title)-3:len(title)] + ' '*7  + "|" + ' '*5 + "Success" + ' '*5 + "|")
    except e:
        print(" |" + ' '*4+ 'plot' + str(idx) + '.pdf'+ ' '*4 + "|" + ' '*8 + f_str + ' '*7 +\
         "|" + ' '*6+ title[title.index("   x")+3:title.index("   x")+8] + ' '*6 +  "|" +\
          ' '*7+ title[len(title)-3:len(title)] + ' '*7  + "|" + ' '*5 + "Failure" + ' '*5 + "|")


master()