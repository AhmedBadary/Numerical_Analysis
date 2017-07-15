# Name: Ahmad Thabet Mohammad Badary
# SID: 25822346
# Date: Jul 10 2017

import numpy as np, math as m

def lagrange(xin,yin,xout):
    ans = 0
    for k in range(len(xin)):
        numerator, denomenator = 1, 1
        for i in range(len(xin)):
            numerator *= (xout - xin[i]) if i!=k else 1
            denomenator *= (xin[k] - xin[i]) if i!=k else 1
        ans += numerator/denomenator * yin[k]
    return ans