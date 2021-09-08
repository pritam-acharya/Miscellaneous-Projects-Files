import matplotlib.pyplot as plt
import numpy as np
import math as mt
X = []
Y = []
for r in np.linspace(0, 4, 10000):
    if r == 1:
        continue
    x = 0.4
    y = []
    while True:
        print(r)
        if x not in y:
            y.append(x)
        else:
            c = y.index(x)
            y = y[c:]
            break
        x=mt.floor(r*x*(1-x)*10**4)/10**4
    for i in y:
        X.append(r)
        Y.append(i)
plt.scatter(X, Y, s=0.01)
plt.show()
