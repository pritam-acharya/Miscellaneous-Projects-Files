import numpy as np
import matplotlib.pyplot as plt
import math
import random

# 3x3 multiplication
# arr1 = []
# arr2 = []

# # matrix 1
# for i in range(0,3):
#     print('row', i+1)
#     m = []
#     for j in range(0,3):
#         k = int(input('enter value {} of row {}: '.format(j+1, i+1)))
#         m.append(k)
#     arr1.append(m)

# # matrix 2
# for i in range(0,3):
#     print('row', i+1)
#     m = []
#     for j in range(0,3):
#         k = int(input('enter value {} of row {}: '.format(j+1, i+1)))
#         m.append(k)
#     arr2.append(m)

# arr1 = np.array(arr1)
# arr2 = np.array(arr2)

# arr3 = np.dot(arr1, arr2) #used to multiply two matrices of the form n*m m*p
# print(arr3)

# # height vs time graph

# # 1. same initial velocity and different angles
# vi = float(input('enter initial velocity in m/s: '))
# g = 9.8 # m/s^2

# theta = np.arange(0,90,15)
# theta_radians = np.radians(theta)
# color_list = ['cyan', 'red', 'yellow', 'purple', 'pink', 'black']

# for angle in theta_radians:
#     time_of_flight = (2 * vi * math.sin(angle)) / g
#     times = np.linspace(0, time_of_flight, 100)
#     heights = np.array((vi * math.sin(angle) * times) - 0.5 * (g * (times ** 2)))
#     colour = random.choice(color_list)
#     color_list.remove(colour)
#     plt.plot(times, heights, color = colour, label = 'Θ = ' + str(round(math.degrees(angle))))

# plt.xlabel('time [s]')
# plt.ylabel('height [m]')
# plt.legend(loc = 'best')
# plt.show()

# # 2. same angle of projection but different initial velocities
# angle = math.radians(float(input('enter initial velocity in degrees: ')))
# g = 9.8 # m/s^2

# velocities = np.arange(0,60,10)
# color_list = ['cyan', 'red', 'yellow', 'purple', 'pink', 'black']

# for vi in velocities:
#     time_of_flight = (2 * vi * math.sin(angle)) / g
#     times = np.linspace(0, time_of_flight, 100)
#     heights = np.array((vi * math.sin(angle) * times) - 0.5 * (g * (times ** 2)))
#     colour = random.choice(color_list)
#     color_list.remove(colour)
#     plt.plot(times, heights, color = colour, label = 'v = ' + str(vi))
# plt.xlabel('time [s]')
# plt.ylabel('height [m]')
# plt.legend(loc = 'best')
# plt.show()

# ball-bouncing
hmax = float(input('enter height from which ball is dropped [m]: '))
e = float(input('enter coefficient of restitution (b/w 0 and 1): '))
bounce = int(input('enter number of bounces you want to see the graph for (in integers): '))
g = 9.8 # m/s^2

t = math.sqrt((2 * hmax) / g)

# before the first bounce
times = np.linspace(0, t, 100)
v = -g * times
v0 = np.amin(v)
vb = abs(v0)
plt.plot(times, v, color = 'blue')
prevtimes = t
posttimes = t + 2 * e * t

#after the first bounce
for i in range(1, bounce + 1):
    vm = abs((e * v0))
    times = np.linspace(0, 2 * (e ** i) * t, 100)
    mtimes = np.linspace(prevtimes, posttimes, 100)
    v = vm - g * times
    v0 = np.amin(v)
    plt.plot(mtimes, v, color = 'blue')
    prevtimes = posttimes
    posttimes += 2 * (e ** (i + 1)) * t

plt.ylim([-vb-1, vb+1])
plt.xlim([0, bounce + 1])
plt.xlabel('time [s]')
plt.ylabel('velocity [m/s]')
plt.grid()
plt.show()