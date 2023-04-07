from math import *
import matplotlib.pyplot as plt


min_time_difference = 0.05
max_time_difference = 1
bias = 3.75

def comp(x, y, z):
    return sqrt(x**2 + y**2 + z**2)

def avg(arr):
    return sum(arr)/len(arr)

with open('data.txt', 'r') as f:
    lines = f.readlines()
    times = [line.split(" ->")[0] for line in lines if " ->" in line]


def time_parse(given_time):
    hours, minutes = [int(x) for x in given_time.split(":")[:2] if ":" in given_time]
    seconds, milliseconds = [int(x) for x in given_time.split(":")[2].split(".") if ":" in given_time]
    return hours*3600 + minutes*60 + seconds + milliseconds*0.001

parsed_times = [time_parse(time) for time in times]
time_differences = []

for i in range(1, len(parsed_times)):
    dt = parsed_times[i] - parsed_times[i-1]
    if ((dt > min_time_difference) and (dt < max_time_difference)): #0.05 = 50ms
        time_differences.append(dt)

avg_dt = avg(time_differences)

acc_count = 0
rot_count = 0
temp_count = 0
acc_x_vals = []
acc_y_vals = []
rot_x_vals = []
rot_y_vals = []
temp_x_vals = []
temp_y_vals = []
for i in range(len(lines)):
    l = lines[i]

    if ('Acceleration' in l):
        bulk = l.split('Acceleration X: ')[1]
        acc_x = bulk.split(",")[0]
        acc_y = bulk.split(",")[1].split(" Y: ")[1] #todo
        acc_z = bulk.split(",")[2].split(" Z: ")[1].split(" m/s^2")[0]
        acc = comp(float(acc_x), float(acc_y), float(acc_z))
        acc_count += 1
        acc_x_vals.append(acc_count)
        acc_y_vals.append(acc)
    if ('Rotation' in l):
        bulk = l.split('Rotation X: ')[1]
        rot_x = bulk.split(",")[0]
        rot_y = bulk.split(",")[1].split(" Y: ")[1] #todo
        rot_z = bulk.split(",")[2].split(" Z: ")[1].split(" rad/s")[0]
        rot = comp(float(rot_x), float(rot_y), float(rot_z))
        rot_count += 1
        rot_x_vals.append(rot_count)
        rot_y_vals.append(rot)
    if ('Temperature' in l):
        temp = l.split('Temperature: ')[1].split(" ")[0]
        temp_count += 1
        temp_x_vals.append(temp_count)
        temp_y_vals.append(float(temp))

print(f"Temperature appeared {temp_count} times and the list of temps is {temp_y_vals}.")
print(f"Acceleration appeared {acc_count} times and the list of accelerations is {acc_y_vals}.")
print(f"Rotation appeared {rot_count} times and the list of rotations is {rot_y_vals}.")

plt.scatter(acc_x_vals, acc_y_vals)
plt.show()


# for i in rotation:
#     if (comp(i[0], i[1], i[2]) >= bias):
#         print("large")
#     else:
#         print("small")