from main import comp
import matplotlib.pyplot as plt

times = []
accelerations = []

a = ['a','b','c','d','e','f','g']

print(a[2:5])
input("Press [ENTER] to Continue...")
with open("arduino-data/falling/FallOnBedArduino.TXT") as f:
    lines = f.readlines()
    length = len(lines)
    j = 1
    for i in list(range(length)):
        if "New event" in lines[i]:
            times.append(float(lines[i+1]) / 1000)
            acc_x = float(lines[i+2])
            acc_y = float(lines[i+3])
            acc_z = float(lines[i+4])
            accelerations.append(comp(acc_x, acc_y, acc_z))

plt.title("Magnitude of Acceleration vs. Time")
plt.xlabel("Time (s)") 
plt.ylabel("Acceleration (m/s^2)")
plt.scatter(times, accelerations)
plt.show()