from numpy import linalg as LA
import numpy as np
import matplotlib.pyplot as plt

arr1 = np.array([[0, 2, 1, 1],
                 [0.5, 0, 0, 0], 
                 [0, 0.2, 0, 0],
                 [0, 0, 0.1, 0]])

time = []
t = 0
final = []
while t < 200:
    t = t+1
    
    time.append(t)
    L200 = LA.matrix_power(arr1, t)
    arr2 = np.array([[200], [0], [0], [0]])

    result = np.array([0, 0, 0, 0])
    result = np.matmul(L200, arr2)
    
    # print(result)
    # for r in result:
        # print(f"The result is: {r}")

    ans = np.sum(result)
    print(f"the population for {t}-th generation is: {ans}")
    
    final.append(ans)

reg = []
for i in range(len(final)):
        a = np.log10(final[i])
        reg.append(a)

plt.interactive(False)
plt.xscale("linear")
plt.plot(time, reg, color="black", linewidth=1, linestyle="-")
plt.xlabel("Time Step")
plt.ylabel("Total Population")
plt.show()
