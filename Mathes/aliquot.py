import matplotlib.pyplot as plt
import gmpy2
from gmpy2 import mpz
import mathes
import math
        
# for i in xrange(1, 1000):
# #   aliquot(i)
#     print mathes.aliquot(i, 20)

n = eval(raw_input()) # Try 936, 222
##y = mathes.aliquot(n,40)
##x = range(len(y))
##    
##plt.plot(x, y, 'r-')
##plt.axis([0, max(x), 0, max(y) * 1.2])
##plt.show()
#
x = [0]
seq = [n]
y = [math.log10(n)]

fig, ax = plt.subplots()
plt.show(block=False)

while n > 1:
   n = sum(mathes.factors(n)) - n
   
   if n in seq:
       break
   
   seq.append(n)
   y.append(math.log10(n))
   x.append(x[-1] + 1)
   
   ax.clear()

   plt.plot(x, y, 'r-')
   plt.axis([0, x[-1], 0, max(y) * 1.1])

   fig.canvas.draw()
   fig.canvas.flush_events()

print 'Done!'
plt.show()