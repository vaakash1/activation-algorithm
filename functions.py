from copy import deepcopy
from math import *

def comp(x, y, z):
    """returns magnitude of the vector <x, y, z>"""
    return sqrt(x**2 + y**2 + z**2)

def allUnderValue(arr, check):
    """"checks if all the values in arr are less than check. Returns true if so and false otherwise"""
    for i in arr:
        if i > check: 
            return False
    return True

def getSlope(arr_a, arr_t, indexAt, depth):
    """"""
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

def cnvd(num_str: str, lineNumber: int):
    try:
        return float(num_str.split('\n')[0])
    except:
        print(f"There was a weird input {num_str} at line {lineNumber}.")

def cnv(num_str: str):
    return float(num_str.split('\n')[0])
class Entry:
    """A class that stores line number, time, 3 dimensions of acceleration, and 3 dimensions of rotation"""
    def __init__(self, time: float, acc_x: float, acc_y: float, acc_z: float, rot_x: float, rot_y: float, rot_z: float, line = 0):
        self.line = line
        self.time = time
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_z = acc_z
        self.rot_x = rot_x
        self.rot_y = rot_y
        self.rot_z = rot_z
        self.acc = comp(acc_x, acc_y, acc_z)
        self.rot = comp(rot_x, rot_y, rot_z)

    def __str__(self) -> str:
        return f'ENTRY DATA at time {self.time} and line {self.line}: Accelerations: {self.acc}\nRotations: {self.rot}\n'

    def is_between(self, lower, upper):
        if (lower < self.line) and (self.line < upper):
            return True
        return False
 
class Batch:
    """"Stores lists of 15 entries that is an input for the ML model"""
    def __init__(self, listOfEntries: list[Entry], falling, first_line = 0):
        self.entries = listOfEntries
        self.falling = falling
        self.fl = first_line

    def __str__(self) -> str:
        result = f"BATCH DATA from line {self.fl}:\nFALLING STATUS: {self.falling}\n"
        input("batch: press enter to continue")
        for entry in self.entries:
            result += entry.__str__()
            result += "\n"
        return result

    def activate(self):
        self.falling = 1

e1 = Entry(1, 0.1, 0, 0, 0, 0, 1, 0)
e2 = Entry(2, 0.2, 0, 0, 0, 0, 0, 0)
e3 = Entry(3, 0.3, 0, 0, 0, 0, 0, 0)
e4 = Entry(4, 0.4, 0, 0, 0, 0, 0, 0)
e5 = Entry(5, 0.5, 0, 0, 0, 0, 0, 0)
e6 = Entry(6, 0.6, 0, 0, 0, 0, 0, 0)
e7 = Entry(1, 0.7, 0, 0, 0, 0, 0, 0)
e8 = Entry(90, 0.8, 0, 0, 0, 0, 0, 0)
e9 = Entry(1, 0.991, 0, 0, 0, 0, 0, 0)
e10 = Entry(1, 0.1, 0, 0, 0, 0, 0, 0)
e11 = Entry(1, 0.1, 0, 0, 0, 0, 0, 0)
e12 = Entry(1, 0.1, 0, 0, 0, 0, 0, 0)
e13 = Entry(1, 0.1, 0, 0, 0, 0, 0, 0)
e14 = Entry(1, 0.1, 0, 0, 0, 0, 0, 0)
e15 = Entry(1, 0.1, 0, 0, 0, 0, 0, 0)

arr_entries = [e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12, e13, e14, e15]

tester = Batch(arr_entries, 0, arr_entries[0].line)
print(tester.falling)
# tester.falling = 1
# tester.activate()
# print(tester.falling)

for entry in tester.entries:
    print(entry.rot)
    if entry.rot > 0:
        tester.activate()

print(tester.falling)
# class Number:
#     def __init__(self, num: int):
#         self.num = num
    
    # def is_between(self, lower, upper):
    #     if (lower < self.num) and (self.num < upper):
    #         return True
    #     return False

# my_num = Number(5)

# print(my_num.is_between(4, 7))

