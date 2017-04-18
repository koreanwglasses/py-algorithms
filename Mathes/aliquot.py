import matplotlib.pyplot as plt
import gmpy2
from gmpy2 import mpz
import mathes
import math

## Just print some aliquot sequences     
# for i in xrange(1, 1000):
#     aliquot(i)
#     print mathes.aliquot(i, 20)

# Take an input
n = eval(raw_input()) # Try 936, 222

## Plot an aliquot sequence
#y = mathes.aliquot(n,40)
#x = range(len(y))
#    
#plt.plot(x, y, 'r-')
#plt.axis([0, max(x), 0, max(y) * 1.2])
#plt.show()
#

## Plot an aliquot sequence in real time (slower, but more fun to watch)

# x-axis: steps
x = [0]

# seq: the aliquot sequence
seq = [n]

# The sequence on the graph, with (or without) transformations
# y = [math.log10(n)]
y = [n]

# initialize plot
fig, ax = plt.subplots()
plt.show(block=False)

# the sum of the factors of 1 == 1 so stop there
while n > 1:
   # let n be the sum of its proper factors 
   n = sum(mathes.factors(n)) - n
   
   # is n is already in the sequence, we know it will repeat, so stop
   if n in seq:
       break
   
   # otherwise add n to the sequence
   seq.append(n)
#  y.append(math.log10(n))
   y.append(int(n))
   x.append(x[-1] + 1)
   
   # redraw plot
   ax.clear()

   plt.clf()

   plt.plot(x, y, 'r-')
   plt.axis([0, x[-1], 0, max(y) * 1.1])

   fig.canvas.draw()
   fig.canvas.flush_events()

print 'Done!'

# keep plot open
plt.show()