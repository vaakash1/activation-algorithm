from math import *

acceleration = [[-7.17, -3.17, 6.27], [-5.22, -7.12, 4,72], [-55.44, 14.26, -8.52]]
rotation = [[-0.01, -0.04, 0.03], [-1.43, 1.82, 5.32], [3.47, 0.73, -8.73]]

bias = 3.75

def comp(x, y, z):
    return sqrt(x**2 + y**2 + z**2)

for i in rotation:
    if (comp(i[0], i[1], i[2]) >= bias):
        print("large")
    else:
        print("small")