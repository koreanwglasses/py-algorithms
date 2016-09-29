import matplotlib.pyplot as plt
import math
import mpmath
import gmpy2
from gmpy2 import mpz

m = 10000

x = [0]
y = [0]

lastn = 2
n = 2
for i in xrange(1,m):
    n = gmpy2.next_prime(n)
    x.append(int(n))
    y.append(1. / int(n - lastn))
    lastn = n
    
    if i % (m // 100) is 0:
        print str(i * 100 // m) + '%'
    
plt.plot(x, y, 'r-')
plt.axis([3, x[-1], 0, max(y)])
plt.show()