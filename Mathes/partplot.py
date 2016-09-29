import mathes3 as mathes
import matplotlib.pyplot as plt
import math

x = []
y = []
plt.show()
for i in range(100):
    x.append(i)
    y.append(math.log(mathes.partitions(i)) ** 2)
    
    plt.plot(x, y, 'r-')
    plt.axis([0, x[-1], 0, y[-1]])
    plt.pause(.01)
print(len(mathes.partitions_moize))
plt.show()