from math import *
import matplotlib.pyplot as plt
import os
from copy import deepcopy
import time
START_TIME = time.time()
min_time_difference = 0.05
max_time_difference = 1
bias = 3.75

def comp(x, y, z):
    return sqrt(x**2 + y**2 + z**2)

def get_range(accelerations):
    return (max(accelerations) - min(accelerations))

def avg(arr):
    return sum(arr)/len(arr)

def convert(scientific):
    if "E" not in scientific:
        return scientific
    parts = scientific.split("E")
    base = float(parts[0])
    exponent = int(parts[1])
    return base * pow(10, exponent)

def jerk(a1, a2, t1, t2):
    return (a2 - a1) / (t2 - t1)

def global_min(arr: list, sampleRate): #NOTE: Returns a list of [min, place]
    min = arr[0]
    min_i = 0
    for i in arr:
        if arr[i] < min:
            min = arr[i]
            min_i = i
    return [min, min_i]
    

def avg_jerk(accelerations, times):
    s = len(accelerations)
    jerks = []
    for i in range(s - 1):
        jerks.append(jerk(accelerations[i], accelerations[i+1], times[i], times[i+1]))
    return avg(jerks)    

with open('arduino-data/misc/orig-data.txt', 'r') as f:
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
        # print(bulk)
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

# print(f"Temperature appeared {temp_count} times and the list of temps is {temp_y_vals}.")
# print(f"Acceleration appeared {acc_count} times and the list of accelerations is {acc_y_vals}.")
# print(f"Rotation appeared {rot_count} times and the list of rotations is {rot_y_vals}.")

# UNCOMMENT THIS TO GRAPH ARDUINO DATA 04.07.23
# emDash = u'\u2014'
# graphTitle = "Magnitude of Acceleration vs. Trial # {0} vigorousShaking".format(emDash)
# plt.title(graphTitle)
# print(f"Magnitudes: {acc_y_vals}")
# plt.title("Magnitude of Acceleration vs. Trial #")
# plt.xlabel("Trial #") 
# plt.ylabel("Acceleration (m/s^2)")
# plt.scatter(acc_x_vals, acc_y_vals)
# plt.savefig("images/data/arduino/walkingData2.png")
# plt.show()

#

# for i in rotation:
#     if (comp(i[0], i[1], i[2]) >= bias):
#         print("large")
#     else:
#         print("small")
# input("press enter to continue ... ")
def graph(filepath):
    times = []
    overall_acc = []
    with open(filepath, "r") as w:
        lines = w.readlines()
        for l in lines[1:]:
            parts = l.split(",")
            times.append(convert(parts[0]))
            overall_acc.append(convert(parts[4]))

    plt.title("Magnitude of Acceleration vs. Time")
    plt.scatter(times, overall_acc)
    # plt.savefig(f"images/figure_falling_{n}.png")
    plt.show()


# graph("phyphox-data/walking/walking_1.csv")
fallingFiles = "phyphox-data/falling"
fallingFilesList = os.listdir(fallingFiles)
fallingFilesNum = len(os.listdir(fallingFiles))
"""
for i in range(1, fallingFilesNum + 1):
    fileName = f"{fallingFiles}/falling_{i}.csv"
    print(fileName)
    graph(fileName, i)
"""


def complexFalling(csv_file):
    with open(csv_file, "r") as f:
        lines = f.readlines()
        times = [convert(l.split(",")[0]) for l in lines[1:]]
        absolutes = [convert(l.split(",")[4]) for l in lines[1:]]
        started = False
        st_num = 0
        stChange = True
        endChange = True
        slopes = []
        end_num = 0
        ended = False
        # mission_critical = 0
        i = 0
        step = 15 #can be adjusted
        while (not started) and (not ended) and (i < (len(lines) - (step  -2))):
            slope = avg_jerk(absolutes[i:i+step], times[i:i+step])
            slopes.append(slope)
            if (slope < -10 and stChange):
                st_num = i/100
                stChange = False
            if (slope > 100 and endChange):
                end_num = i/100
                endChange = False
                
            # if (slope < -30):
            #     mission_critical = slope
            # if (slope > 150):
            #     end_num = slope
            # print(f"Slope when i equals {i}: {slope} m/s^3")
            # print(f"status at i equals {i}: {(slope < -9)}")
            i += 1
        # print(len(slopes))
        # print(len(list(range(len(lines) - step + 2))))
        # plt.scatter(list(range(len(lines) - step + 2)), slopes)
        # plt.show()
    # print(f"Start time: {st_num}s")
    # print(f"End time: {end_num}s")
    start_i = int(st_num * 100)
    end_i = int(end_num * 100)
    # print(f"Start acceleration: {absolutes[start_i]} m/s^2")
    # print(f"End acceleration: {absolutes[end_i]} m/s^2")
    return [absolutes[start_i], absolutes[end_i]]


#running complex falling
start_accelerations = []
end_accelerations = []
for s in fallingFilesList:
    filename = f"{fallingFiles}/{s}"
    A_both = complexFalling(filename)
    start_accelerations.append(A_both[0])
    end_accelerations.append(A_both[1])
# print(f"Start accelerations: {start_accelerations}")
# print(f"End accelerations: {end_accelerations}")
# print(f"AVG. START ACCELERATION: {avg(start_accelerations)}")
# print(f"AVG. END ACCELERATION: {avg(end_accelerations)}")
#complexFalling("phyphox-data/falling/falling_3.csv")

def allUnderValue(arr, check):
    for i in arr:
        if i > check: 
            return False
    return True
    
def getSlope(arr_a, arr_t, indexAt, depth):
    return (arr_a[indexAt] - arr_a[indexAt - depth])/(arr_t[indexAt] - arr_t[indexAt - depth])


def simpleFalling(dataFilePath):
    latency = 10 #How many terms should I check behind
    max_a = 9.35 #max falling acceleration
    with open(dataFilePath, 'r') as d:
        lines = d.readlines()
        times = [convert(l.split(",")[0]) for l in lines[1:]]
        absolutes = [convert(l.split(",")[4]) for l in lines[1:]]
        condition1 = False #checks for magnitude
        condition2 = False #checks for slope
       #while ((not condition1) and (not condition2)):
        current = deepcopy(latency)
        #print(current)
        for a in absolutes[latency:]:
            if a < max_a and allUnderValue(absolutes[current - latency: current], max_a) and not condition1:
                condition1 = True
                print(f"FILE NAME: {dataFilePath}")
                print(f"Time for magnitude success: {times[current]}s.")
                # print(f"Magnitude for magnitude success: {absolutes[current]} m/s^2.")
                print(f"Slope for magnitude success: {getSlope(absolutes, times, current, latency)} m/s^3.\n")
                condition1 = True
                return times[current]
            current += 1
    
def simpleFallingWithoutFile(times, absolutes):
    latency = 10 #How many terms should I check behind
    max_a = 9.35 #max falling acceleration
    good_times = []
    slopeCheck = -3
    # condition1 = False #checks for magnitude
    # condition2 = False #checks for slope
    current = deepcopy(latency)
    for a in absolutes[latency:]:
            if a < max_a and allUnderValue(absolutes[current - latency: current], max_a) and getSlope(absolutes, times, current, latency) < slopeCheck:
                print(f"Time for magnitude success: {times[current]}s.")
                # print(f"Magnitude for magnitude success: {absolutes[current]} m/s^2.")
                # print(f"Slope for magnitude success: {getSlope(absolutes, times, current, latency)} m/s^3.\n")
                good_times.append(times[current])
            current += 1
    return good_times


for FileName in fallingFilesList:
    actualPath = f"{fallingFiles}/{FileName}"
    print(f"File Path: {actualPath}")
    simpleFalling(actualPath)

#checking runtime
END_TIME = time.time()
print(f"main.py Runtime: {END_TIME-START_TIME}s")
