import matplotlib.pyplot as plt
import math
import mpmath
import gmpy2
from gmpy2 import mpz

m = 1000000

x = [0]
y = [0]

n = 1
for i in xrange(1,m):
    n = gmpy2.next_prime(n)
    x.append(int(n))
    y.append(i)
    
    if i % (m // 100) is 0:
        print str(i * 100 // m) + '%'
    
plt.plot(x, y, 'r-')
plt.axis([4, x[len(x) - 1], 0, y[len(y) - 1]])
plt.show()