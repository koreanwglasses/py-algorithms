max_iter = 1000

bounds = (-1.5, -1, .5, 1) # left, bottom, right, top

### --- Complex Methods --- ###
def mag2(c):
    r, i = c
    return r * r + i * i

def mult(c1, c2):
    r1, i1 = c1
    r2, i2 = c2
    return (r1 * r2 - i1 * i2, r1 * i2 + i1 * r2)

def add(c1, c2):
    r1, i1 = c1
    r2, i2 = c2
    return (r1 + r2, i1 + i2)

def next_complex():
    z = (random.random() * 4 - 2, random.random() * 4 - 2)
    while True:
        z = (random.random() * 4 - 2, random.random() * 4 - 2)
        
        x, y = z
        q = (x - .25) * (x - .25) + y * y 
        if mag2(z) < 4 and (x + 1) * (x + 1) + y * y < 1/16 and q * (q + (x - .25)) < y * y * .25:      
            return z

### --- Bounds Methods --- ###
def in_bounds(bounds, point):
    x, y = point
    l, b, r, t = bounds
    return x >= l and x < r and y >= b and y < t

### --- Sampling Functions --- ###
def sample(c):
    visited = []
    z = (0,0)
    for _ in range(max_iter):
        z = add(mult(z, z), c)
        if mag2(z) > 4:
            return visited
        elif in_bounds(bounds, z):
            visited.append(point_to_bin(bounds, height, width, z))
    return []

def contrib(c):
    visited = 0
    z = (0,0)
    for _ in range(max_iter):
        z = add(mult(z, z), c)
        if mag2(z) > 4:
            break
        elif in_bounds(bounds, z):
            visited += 1
    return 0