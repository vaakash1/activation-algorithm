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


# class Number:
#     def __init__(self, num: int):
#         self.num = num
    
    # def is_between(self, lower, upper):
    #     if (lower < self.num) and (self.num < upper):
    #         return True
    #     return False

# my_num = Number(5)

# print(my_num.is_between(4, 7))

