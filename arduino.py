from main import comp, simpleFallingWithoutFile
import matplotlib.pyplot as plt
import time
st = time.time()


times = []
accelerations = []
temp_times = []
temp_accelerations = []

def global_minimum(t_vals, a_vals):
    min_i = 0
    min_a = a_vals[0]
    for i in range(len(a_vals)):
        if (a_vals[i]) < min_i:
            min_a = a_vals[i]
            min_i = i
    return [min_a, min_i] # returns min acceleration and minimum i

fileName = "arduino-data/walking/walkingWithFannyPack.TXT"
mid = fileName.split("/")[-2]
extension = fileName.split('/')[-1].split(".")[0]

with open(fileName) as f:
    lines = f.readlines()
    length = len(lines)
    j = 1
    for i in range(1, len(lines)):
        if "New Trial" in lines[i]:
            times.append(temp_times)
            accelerations.append(temp_accelerations)
            plt.title("Magnitude of Acceleration vs. Time")
            plt.xlabel("Time (s)") 
            plt.ylabel("Acceleration (m/s^2)")
            plt.scatter(temp_times, temp_accelerations)
            plt.savefig(f"images/data/arduino/{mid}/{extension}{j}.png")
            plt.show()
            s = simpleFallingWithoutFile(temp_times, temp_accelerations)
            # global_minimum(temp_times, temp_accelerations)
            print(f"falling of file {j}: {s}")
            temp_times.clear()
            temp_accelerations.clear()
            j += 1
        if "New event" in lines[i]:
            temp_times.append(float(lines[i+1]) / 1000)
            acc_x = float(lines[i+2])
            acc_y = float(lines[i+3])
            acc_z = float(lines[i+4])
            temp_accelerations.append(comp(acc_x, acc_y, acc_z))


print(len(times))
print(len(accelerations))

class Entry:
    def __init__(self, time, acc_x, acc_y, acc_z, rot_x, rot_y, rot_z):
        self.time = time
        self.acc_x = acc_x
        self.acc_y = acc_y
        self.acc_z = acc_z
        self.rot_x = rot_x
        self.rot_y = rot_y
        self.rot_z = rot_z
        acc_magnitude = comp(acc_x, acc_y, acc_x)
        rot_magnitude = comp(rot_x, rot_y, rot_z)





#ending code
end = time.time()
print(f"arduino.py runtime: {end-st}s")