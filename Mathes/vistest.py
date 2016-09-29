import random
import matplotlib.pyplot as plt

def dst2(a, b):
    ax, ay = a
    bx, by = b
    return (bx - ax) * (bx - ax) + (by - ay) * (by - ay)

def proximity(points, candidate, r):
    for point in points:
        if dst2(point, candidate) < r * r:
            return False
    return True

def nextpoint(points, r, bounds, attempts=100):    
    for _ in range(attempts):
        candidate = (random.uniform(bounds[0], bounds[1]), random.uniform(bounds[2], bounds[3]))
        if proximity(points, candidate, r):
            return candidate        
    return None

def poisson(n, r, bounds=[0, 1, 0, 1]):
    points = []
    
    for _ in range(n):
        point = nextpoint(points, r, bounds)
        if point != None:
            points.append(point)
        else:
            break
    return points

points = poisson(100, .05)

plt.show()
xs, ys = zip(*points)
plt.plot(xs,ys,'ro')
plt.axis([0, 1, 0, 1])
plt.show()