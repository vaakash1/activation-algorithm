from main import comp, simpleFalling
import matplotlib.pyplot as plt

times = []
accelerations = []
temp_times = []
temp_accelerations = []


with open("arduino-data/falling/FallOnBedArduino.TXT") as f:
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
            #plt.savefig(f"images/data/arduino/falling/fallingData{j}.png")
            plt.show()
            if j == 3:
                print(temp_times)
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

