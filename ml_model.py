# put all falling data into CSV file
from copy import deepcopy
from math import *

with open(r'arduino-data\falling\FallOnBedArduino.TXT', 'r') as f:
    lines = f.readlines()

def comp(x, y, z):
    return sqrt(x**2 + y**2 + z**2)

def allUnderValue(arr, check):
    for i in arr:
        if i > check: 
            return False
    return True

def getSlope(arr_a, arr_t, indexAt, depth):
    return (arr_a[indexAt] - arr_a[indexAt - depth])/(arr_t[indexAt] - arr_t[indexAt - depth])

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
               #  print(f"Time for magnitude success: {times[current]}s.")
                # print(f"Magnitude for magnitude success: {absolutes[current]} m/s^2.")
                # print(f"Slope for magnitude success: {getSlope(absolutes, times, current, latency)} m/s^3.\n")
                good_times.append(times[current])
            current += 1
    return good_times



def global_minimum(t_vals, a_vals):
    min_i = 0
    min_a = a_vals[0]
    for i in range(len(a_vals)):
        if (a_vals[i]) < min_i:
            min_a = a_vals[i]
            min_i = i
    return [min_a, min_i] # returns min acceleration and minimum i

def check_file(fileName):
    times = []
    accelerations = []
    #temp_times = []
    #temp_accelerations = []
    rotations = []
    #temp_rotations = []
    markers = []
    with open(fileName) as f:
        lines = f.readlines()
        i = 0
        for line in lines:
            if "New Trial" in line:
                markers.append(i)
                print(i)
            i += 1

    class Entry:
        def __init__(self, time, acc_x, acc_y, acc_z, rot_x, rot_y, rot_z):
            self.time = time
            self.acc_x = acc_x
            self.acc_y = acc_y
            self.acc_z = acc_z
            self.rot_x = rot_x
            self.rot_y = rot_y
            self.rot_z = rot_z
            self.acc = comp(acc_x, acc_y, acc_z)
            self.rot = comp(rot_x, rot_y, rot_z)
            self.did_fall = False


    j = 0
    for marker in markers:
        lines_u = lines[marker: markers[j+1]]
        entries = []
        try:
            for i in range(len(lines_u)):
                if 'New event' in lines_u[i]:
                    entries.append(Entry(lines_u[i + 1], lines_u[i + 2], lines_u[i + 3], lines_u[i + 4]))
        except:
            print("you tried")
            print("There were no events")
        j += 1
        # lines = f.readlines()
        # j = 1
        # for i in range(1, len(lines)):
        #     if "New Trial" in lines[i]:
        #         times.append(temp_times)
        #         accelerations.append(temp_accelerations)
        #         rotations.append(temp_rotations)
        #         s = simpleFallingWithoutFile(temp_times, temp_accelerations)
        #         # global_minimum(temp_times, temp_accelerations)
        #         # print(f"falling of file {j}: {s}")
        #         temp_times.clear()
        #         temp_accelerations.clear()
        #         temp_rotations.clear()
        #         j += 1
        #     if "New event" in lines[i]:
        #         try:
        #             acc_x = float(lines[i+2])
        #             acc_y = float(lines[i+3].split("\n")[0])
        #             acc_z = float(lines[i+4])
        #             rot_x, rot_y, rot_z = float(lines[i+5]), float(lines[i+6]), float(lines[i+7])
        #             temp_rotations.append(comp(rot_x, rot_y, rot_z))
        #             temp_times.append(float(lines[i+1]) / 1000)
        #             temp_accelerations.append(comp(acc_x, acc_y, acc_z))
        #         except:
        #             print("You tried, it's ok!")
        #             print(i)
        # return [times, times, times]
    
check_file(r'arduino-data\falling\Sumanth_falling_5_10_23.TXT')

