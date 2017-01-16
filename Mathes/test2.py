import math
s = 0
s_last = -1
for n in range(2, 10000000):
    s_last = s
    s += (-1)**n / math.log(n)
print 0.5 * (s + s_last)
