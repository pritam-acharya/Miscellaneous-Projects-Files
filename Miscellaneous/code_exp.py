# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 19:01:38 2021

@author: adity
"""

import numpy as np
import matplotlib.pyplot as plt
import csv

def equalize(x_v, y_v):
    if len(x_v) != len(y_v):
        if len(x_v) > len(y_v):
            while len(x_v) != len(y_v):
                y_v.append(y_v[len(y_v) - 1])
        else:
            while len(x_v) != len(y_v):
                x_v.append(x_v[len(x_v) - 1])
    return x_v, y_v

def bestfit(x_values, y_values):
    x_values, y_values = equalize(x_values, y_values)
    N = len(y_values)
    #print(N)
    ind_1 = 0
    ind_2 = 0
    ind_3 = 0
    ind_4 = 0
    A = 0
    B = 0
    C = 0
    D = 0
    
    #A
    while ind_1 < N:
        A = A + (x_values[ind_1] * x_values[ind_1])
        ind_1 = ind_1 + 1
    #B
    while ind_2 < N:
        B = B + x_values[ind_2] 
        ind_2 = ind_2 + 1
        
    #C
    while ind_3 < N:
        C = C + x_values[ind_3] * y_values[ind_3]
        ind_3 = ind_3 + 1
        
    #D
    while ind_4 < N:
        D = D + y_values[ind_4] 
        ind_4 = ind_4 + 1
        
    b_1 = ((B*C) - (D*A))/((B*B)-(A*N))
    
    a_1 = (C - (B * b_1)) / A
    
    det = A * N - B**2
    
    #print(f'{a}  {b}')
    #print(A)
    #print(B)
    #print(C)
    #print(D)
    
    if det == 0:
        print("couldn't find the line of best fit")
    else:
        x_axis = np.array(x_values)
        y_axis = np.array(y_values)
        
        new_y_axis = a_1 * x_axis + b_1
        
        plt.plot(x_axis, y_axis, 'bo', ms = 1.5, color = 'pink')
        plt.plot(x_axis, new_y_axis, color = 'red')

def plotit(n,m):
    n, m = equalize(n,m)
    plt.plot(n, m, '-', color = 'black')

time = []
disp = []

#so from tracker copy the table into excel and just save the colmuns of numbers as csv, then insert file location here
with open(r'C:\Users\adity\Desktop\IISER acad\SEM 3\LAB\K2\Graphs\20mm.csv') as csv_file:
  csv_reader = csv.reader(csv_file, delimiter = ',')
  for col in csv_reader:
    time.append(float(col[0]))
    disp.append(float(col[1]))
    
def differ(func):
    len_f = len(func)
    diff = []
    k1 = 0
    k2 = 1
    
    while k2 < len_f:
        accl = (func[k2] - func[k1]) / (time[k2] - time[k1])
        diff.append(accl)
        k1 = k1 + 1
        k2 = k2 + 1
    
    return diff
    
a = 0
b = 1
len_d = len(disp)
vel = []
v = 0
disp_plot =[]
k = 0
#while k<100:
#    disp_plot.append(disp[k])
#    k = k + 1

while b < len_d:
    v = (disp[b] - disp[a]) / (time[b] - time[a])
    vel.append(v)
    b = b + 1
    a = a + 1
    
len_v = len(vel)
vel = differ(disp)
acc = differ(vel)
jerk = differ(acc)
    
#plt.plot(acc, disp, 'bo', ms='1.5')
time, acc = equalize(time, acc)
time, vel = equalize(time, vel)
time, jerk = equalize(time, jerk)

#plt.plot(time, acc, '-', color ='red')
#plt.plot(time, vel, '-', color = "blue")
#plt.plot(disp, vel, '-',ms = '1.5', color ='red')
plt.plot(vel, jerk, 'bo', ms='0.5' , color = 'pink')

#bestfit(disp, acc)   
#bestfit(time, vel)
#bestfit(time, disp)