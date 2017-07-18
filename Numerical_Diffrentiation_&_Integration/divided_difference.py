import numpy as np

def nddp(xin, yin, xout):
    n, ans = len(xin), 0
    F = np.zeros((n, n))
    coeffs = []
    for i in range(n):
        F[i][0] = yin[i]

    for i in range(1, n):
        temp_val = 1
        for j in range(0, i):
            temp_val *= (xout - xin[j])
        coeffs.append(temp_val)

    for i in range(1, n):
        for j in range(1, i+1):
            F[i][j] = ( F[i][j-1] - F[i-1][j-1] ) / (xin[i] - xin[i-j])
        ans += coeffs[i-1]*F[i][i]

    return F[0][0] + ans

# xin = [2,2.2,2.3]
# yin = [0.6931, 0.7885, 0.8329]
# xout = 2.1
# xin = [-.5, -0.25, 0.25, 0.5]
# yin = [1.93750, 1.33203, 0.800781, 0.687500]
# xout = 0
xin = [1,1.3,1.6,1.9,2.2]
yin = [.7651977, .6200860 , .4554022 , .2818186, .1103623]
xout = 1.5