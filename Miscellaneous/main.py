from numpy import linalg as LA
import numpy as np

arr1 = np.array([[0, 2, 1, 1],
                 [0.5, 0, 0, 0],
                 [0, 0.2, 0, 0],
                 [0, 0, 0.1, 0]])
# print("The array is:\n", arr1)
# When n=2

t = 0

while t < 100:
    t = t+1
    L200 = LA.matrix_power(arr1, t)
    # print("Matrix Power is:\n", L200)
    arr2 = np.array([[200], [0], [0], [0]])

    result = [[0],
              [0],
              [0],
              [0]]

    # iterate through rows of X
    for i in range(len(arr1)):
    # iterate through columns of Y
        for j in range(len(arr2[0])):
            # iterate through rows of Y
            for k in range(len(arr2)):
                result[i][j] += arr1[i][k] * arr2[k][j]

    for r in result:
        print(r)
