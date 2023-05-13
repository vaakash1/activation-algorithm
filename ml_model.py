from copy import deepcopy
from math import *
from functions import *

class Entry:
    """A class that stores time, 3 dimensions of acceleration, and 3 dimensions of rotation"""
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

    def is_between(self, lower, upper):
        if (lower < self.line) and (self.line < upper):
            return True
        return False
    
# testEntry = Entry(1, 2, 2, 2, 3, 3, 3)
# print(testEntry.acc)

input("Press enter to continue 1")

filePath = "arduino-data/falling/Venkat_falling_5_9_23.txt"

def make_markers(fileName):
    markers = []
    with open(fileName, "r") as file:
        lines = file.readlines()
        print(lines[:10])
        for i in range(len(lines)):
            if lines[i] == 'New Trial\n':
                markers.append(i)
    return markers

markers = make_markers(filePath)
# print(markers)

def get_entries(fileName):
    entries = []
    with open(fileName, 'r') as file:
        lines = file.readlines()
        for i in range(len(lines)):
            if lines[i] == ' + New event: \n':
                # try:
                #     entry = Entry(cnvd(lines[i + 1], i + 1), cnvd(lines[i + 2], i + 2), cnvd(lines[i + 3], i + 3), cnvd(lines[i + 4], i + 4), cnvd(lines[i + 5], i + 5), cnvd(lines[i + 6], i + 6), cnvd(lines[i + 7], i + 7), line=i)
                #     entries.append(entry)
                # except TypeError:
                #     print(f"There was a problem making the Entry at line {i}.")
                try:
                    entry = Entry(cnv(lines[i + 1]) / 1000, cnv(lines[i + 2]), cnv(lines[i + 3]), cnv(lines[i + 4]), cnv(lines[i + 5]), cnv(lines[i + 6]), cnv(lines[i + 7]), line=i)
                    entries.append(entry)
                except ValueError:
                    print(f"Error occurred in the entry from line {i}.")
    return entries

raw_entries = get_entries(filePath)
input("press enter to continue 2")
#print(raw_entries)

def get_organized_entries(entries: list[Entry], markers: list[int]) -> list[list[Entry]]:
    organized_entries = []
    for i in range(len(markers) - 1):
        trial_entries = []
        for entry in entries:
            if entry.is_between(markers[i], markers[i + 1]):
                trial_entries.append(entry)
        organized_entries.append(trial_entries)
    return organized_entries

organized_entries = get_organized_entries(raw_entries, markers)

class Batch:
    def __init__(self, listOfEntries: list[Entry], falling = False, first_line = 0):
        self.entries = listOfEntries
        self.falling = falling
        self.fl = first_line
        

def get_batches(organized_entries: list[list[Entry]], batch_size = 15) -> list[list[Batch]]:
    batches = []
    for trial_entries in organized_entries:
        trial_batches = []
        if len(trial_entries) < batch_size:
            continue
        for i in range(len(trial_entries) - batch_size):
            trial_batch = Batch(trial_entries[i: i + batch_size], first_line=trial_entries[i].line)
            trial_batches.append(trial_batch)
        batches.append(trial_batches)
    return batches

batches = get_batches(organized_entries)
input('press enter to continue 3')
print(batches[0][0])
# goodEntry = Entry(32, 312, 312, 543, 123, 54, 123)

# print(goodEntry.line)
# print(TypeError)
# badEntry = Entry(32)


# with open(r'arduino-data\falling\FallOnBedArduino.TXT', 'r') as f:
#     lines = f.readlines()



# def make_markers(fileName):
#     times = []
#     accelerations = []
#     rotations = []
#     markers = []
#     with open(fileName) as f:
#         lines = f.readlines()
#         i = 0
#         for line in lines:
#             if "New Trial" in line:
#                 markers.append(i)
#                 # print(i)
#             i += 1
#     return markers




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
    

