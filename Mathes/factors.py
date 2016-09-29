import matplotlib.pyplot as plt 
import numpy as np
import mathes
import math

fig, ax = plt.subplots()
fig.set_tight_layout(True)

ub = 2**20

#-- Fast --#

x = xrange(2, ub)
# y = [mathes.count_factors(n) for n in x]

#-- Log -- #

y = []
for n in x:
    if (n % (ub // 100)) == 0:
        print('{}% ({}/{})'.format(100*n//ub, n, ub))
    y.append(mathes.count_uq_prime_factors(n))

# plt.plot(x, y, 'ro')
# plt.axis([0, max(x), 0, max(y) * 1.1])

#-- Live --#

# plt.show(block=False)

# xs = []
# ys = []
# for x in range(2,10000):
#     xs.append(x)
#     ys.append(mathes.count_factors(x))

#     ax.clear()

#     plt.plot(xs, ys, 'ro')
#     plt.axis([0, max(xs), 0, max(ys) * 1.1])

#     fig.canvas.draw()
#     fig.canvas.flush_events()

#-- Scatterplot Histogram --#

bins = {}
for c in y:
    if c in bins:
        bins[c] = bins[c] + 1
    else:
        bins[c] = 0

bx = range(max(y))
by = []

for x in bx:
    if x in bins:
        by.append(bins[x])
    else:
        by.append(0)

f = open('images/facs.txt', 'a+')
f.write(str(by) + '\n')
print(by)

# plt.plot(bx[::4], by[::4], 'r-')
# plt.axis([0, max(bx), 0, max(by) * 1.1])

#-- Curve --#

def f(x, mu, std, scl):
    return scl * np.exp(-(x-mu)**2/(2 * std ** 2))

devx = np.arange(0, 7, 0.1)
mu = sum([x * by[x] for x in bx]) / float(sum(by))
std = math.sqrt(sum([by[x] * (x - mu) ** 2 for x in bx]) / float(sum(by) - 1))
scl = max(by)
print('mean: {}, std: {}'.format(mu, std))
plt.plot(devx, f(devx,mu,std,scl), 'r-')

#-- Histogram -- #

plt.hist(y, max(y) - 1, log=False)

plt.show()