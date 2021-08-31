# Program to multiply two matrices using nested loops

# 3x3 matrix
X = [[0, 2, 1, 1],
     [0.5, 0, 0, 0],
     [0, 0.2, 0, 0],
     [0, 0, 0.1, 0]]
# 3x4 matrix
Y = [[200],
     [0],
     [0],
     [0]]
# result is 3x4
result = [[0],
          [0],
          [0],
          [0]]

# iterate through rows of X
for i in range(len(X)):
   # iterate through columns of Y
   for j in range(len(Y[0])):
       # iterate through rows of Y
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

for r in result:
   print(r)
