import matplotlib.pyplot as plt
import gmpy2
from gmpy2 import mpz
import mathes
import math

def iterate(c):
    if gmpy2.is_even(c):
        return c >> 1
    else:
        return (c << 1) + c + 1

n = mpz(raw_input())

x = [0]
y = [math.log(int(n), 3)]

plt.show()
while True:
    
    if n < 2:
        break
    
    n = iterate(n)
    y.append(math.log(int(n), 3))
    x.append(x[-1] + 1)
    
    plt.plot(x, y, 'r-')
    plt.axis([0, x[-1], 0, max(y) * 1.1])
    plt.pause(.01)

print 'Done!'
plt.show()