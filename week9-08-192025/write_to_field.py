import numpy as np
import math

def write_to_filed(filename, x,y):
    with open(str(filename) + ".txt", "w") as file:
        for i in range(len(x)):
            file.write(str(x[i]) + "\t" + str(y[i]))
            file.write("\n")

x = np.arange(0, math.pi, 0.01)
y = []
for i in range(len(x)):
    y.append(math.sin(x[i]))
write_to_filed("xy", x,y)