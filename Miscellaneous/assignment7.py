import numpy as np
import matplotlib.pyplot as plt
import csv

x_values = []
y_values = []

with open(r'linear_data_with_noise.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        x_values.append(float(row[1]))
        y_values.append(float(row[2]))

x_values = np.array(x_values)
y_values = np.array(y_values)
N = len(x_values)

# Calculating A
A = 0
for x in x_values:
    A += (x * x)

# Calculating B
B = 0
for x in x_values:
    B += x

# Calculating C
C = 0
for x, y in zip(x_values, y_values):
    C += (x * y)

# Calculating D
D = 0
for y in y_values:
    D += y

a = (C - (B * D) / N) / (A - (B * B) / N)
b = (D - B * a) / N

y = a * x_values + b

plt.plot(x_values, y_values, marker='*', label='(x,y) values', markersize=1.5, linestyle='', color='blue')
plt.xlabel('x values')
plt.ylabel('y values')

plt.plot(x_values, y, label='y=ax+b', color='black', linewidth=2)
plt.legend()
plt.show()
