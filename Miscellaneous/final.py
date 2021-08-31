import numpy as np
import matplotlib.pyplot as plt

trans_matrix = np.array([[0, 2, 1, 1],
                        [0.5, 0, 0, 0],
                        [0, 0.2, 0, 0],
                        [0, 0, 0.1, 0]])

pop_vec_initial = np.array([200, 0, 0, 0])

time_step = np.arange(0, 201, 1)
time_step_for_last = np.arange(0, 200, 1)

#whole_data = np.array([])
#whole_data = np.append(whole_data, pop_vec_initial, axis = 0)
whole_data = pop_vec_initial

for i in range(200):
    pop_vec = np.matmul(trans_matrix, pop_vec_initial)
    whole_data = np.vstack([whole_data, pop_vec])
    pop_vec_initial = pop_vec

total_pop = np.sum(whole_data, axis=1)

print(whole_data)
#print(total_pop)

# Plotting total population vs time
plt.plot(time_step, total_pop, color="cyan")
plt.xlabel("Steps in Time")
plt.ylabel("Total Population")
plt.show()

# Plotting n_x+1 / n_x for x = 1,2,3

ratio_array_1 = np.array([])
ratio_array_2 = np.array([])
ratio_array_3 = np.array([])

for i in range(len(whole_data)):
    ratio_array_1 = np.append(
        ratio_array_1, whole_data[i][1] / whole_data[i][0])

for i in range(len(whole_data)):
    ratio_array_2 = np.append(
        ratio_array_2, whole_data[i][2] / whole_data[i][1])

for i in range(len(whole_data)):
    ratio_array_3 = np.append(
        ratio_array_3, whole_data[i][3] / whole_data[i][2])

#print(ratio_array_1)
plt.figure()
plt.plot(time_step, ratio_array_1, color="red", linewidth=0.7, label="n2/n1")
plt.plot(time_step, ratio_array_2, color="green", linewidth=0.7, label="n3/n2")
plt.plot(time_step, ratio_array_3, color="blue", linewidth=0.7, label="n4/n3")
plt.xlabel("Time Step")
plt.ylabel("Ratio of Age Sizes")
plt.legend()
plt.show()

# Plotting N_t+1 vs N_t
pop_ratio = np.array([])
for i in range(len(total_pop)-1):
    pop_ratio = np.append(pop_ratio, total_pop[i+1]/total_pop[i])

plt.figure()
plt.plot(time_step_for_last, pop_ratio, color="black", linewidth=0.75, linestyle="solid")
plt.xlabel("Time Step")
plt.ylabel("Required ratio")
plt.show()
