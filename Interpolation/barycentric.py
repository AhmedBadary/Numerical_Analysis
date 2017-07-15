# Name: Ahmad Thabet Mohammad Badary
# SID: 25822346
# Date: Jul 10 2017

import numpy as np, math as m

def barycentric(xin, yin, xout):
    if isinstance(xout, list):
        return [barycentric(xin, yin, xout_i) for xout_i in xout]
    l_x_, answer = 1, 0
    xin, yin, xout = [elem.tolist() if isinstance(elem, np.ndarray) else elem for elem in (xin, yin, xout)]
    if xout in xin:
        return yin[xin.index(xout)]
    for x in xin:
        l_x_ *= (xout - x)
    for j in range(len(xin)):
        weights = 1
        for k in range(len(xin)):
            weights *= (xin[j] - xin[k]) if k!=j else 1
        answer += ((1 / weights) / (xout - xin[j])) * yin[j]
    return answer * l_x_