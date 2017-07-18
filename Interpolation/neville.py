import numpy as np

def neville(xin, yin, xout):
    n = len(xin)
    Q = np.zeros((n, n))
    for i in range(n):
        Q[i][0] = yin[i]

    for i in range(1, n):
        for j in range(1, i+1):
            Q[i][j] = ( (xout - xin[i-j]) * Q[i][j-1] )
            Q[i][j] -= ((xout - xin[i])*Q[i-1][j-1])
            Q[i][j] /= (xin[i] - xin[i-j])
    return Q

# xin = [2,2.2,2.3]
# yin = [0.6931, 0.7885, 0.8329]
# xout = 2.1
# xin = [-.5, -0.25, 0.25, 0.5]
# yin = [1.93750, 1.33203, 0.800781, 0.687500]
# xout = 0
xin = [1,1.3,1.6,1.9,2.2]
yin = [.7651977, .6200860 , .4554022 , .2818186, .1103623]
xout = 1.5

def print_mat(Q):
    for i in range(Q.shape[0]):
        for j in range(Q.shape[0]):
            if (Q[i][j] == 0):
                continue
            print("Q "+str(i)+","+str(j)+" = ", Q[i][j])
