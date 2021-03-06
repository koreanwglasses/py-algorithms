from PIL import Image
import random
from multiprocessing import Pool
import itertools

height = 1200
width = 1200

max_iter = 10000
samples = 2 ** 10 # 2 ** 20
threads = 2 ** 3
runs = 8 * threads

check_interval = samples * runs // 100

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

### --- Bounds Methods --- ###
def in_bounds(bounds, point):
    x, y = point
    l, b, r, t = bounds
    return x >= l and x < r and y >= b and y < t

### --- Main Program Methods --- ###
def point_to_bin(bounds, width, height, point):
    x, y = point
    l, b, r, t = bounds
    return (int((x - l) * width // (r - l)), int((y - b) * height // (t - b)))

edge_grid = [(-2.9, 0.0), 
             (-1.9, 0.0), 
             (-1.8, 0.0), 
             (-1.7, 0.0), 
             (-1.6, 0.0), 
             (-1.5, 0.0), 
             (-1.4, 0.0), 
             (-1.3, 0.0), (-1.3, 0.3),
             (-1.2, 0.1), (-1.2, 0.2), (-1.2, 0.3), 
             (-1.1, 0.2), (-1.1, 0.3),
             (-1.0, 0.2), (-1.0, 0.3),
             (-0.9, 0.1), (-0.9, 0.2), 
             (-0.8, 0.0), (-0.8, 0.1), (-0.8, 0.2), (-0.8, 0.3), 
             (-0.7, 0.2), (-0.7, 0.3), (-0.7, 0.4), 
             (-0.6, 0.4), (-0.6, 0.5), (-0.6, 0.6), 
             (-0.5, 0.5), (-0.5, 0.6),
             (-0.4, 0.5), (-0.4, 0.6),
             (-0.3, 0.6), (-0.3, 0.7), (-0.3, 0.8),
             (-0.2, 0.6), (-0.2, 0.7), (-0.2, 0.8), (-0.2, 0.9), (-0.2, 1.0), 
             (-0.1, 0.6), (-0.1, 0.7), (-0.1, 0.8), (-0.1, 0.9), 
             (0.0, 0.6), 
             (0.1, 0.5), (0.1, 0.6),
             (0.2, 0.0), (0.2, 0.4), (0.2, 0.5), (0.2, 0.6),
             (0.3, 0.0), (0.3, 0.1), (0.3, 0.2), (0.3, 0.3), (0.3, 0.4), (0.3, 0.5), (0.3, 0.6), 
             (0.4, 0.2), (0.4, 0.3)]
edge_grid_res = 0.1
def edge_grid_point():
    x, y = random.choice(edge_grid)
    x = x + random.random() * edge_grid_res
    y = y + random.random() * edge_grid_res
    if 0.5 < random.random():
        return (x, -y)
    else:
        return (x, y)

def next_complex():
    while True:
        z = edge_grid_point() #(random.random() * 4 - 2, random.random() * 4 - 2)
        
        x, y = z
        q = (x - .25) * (x - .25) + y * y
        in_circle = mag2(z) < 4
        in_cardioid = q * (q + (x - .25)) < y * y * .25
        in_bulb = (x + 1) * (x + 1) + y * y < 1/16
        if in_circle and not in_bulb and not in_cardioid:
            if pre_sample(z) > (max_iter // 20):
                return z
        
def pre_sample(c):
    iterations = 0
    z = (0,0)
    for _ in range(max_iter):        
        z = add(mult(z, z), c)
        if(mag2(z) > 4):
            return iterations
        else:
            iterations += 1
    return 0
    
def sample(index):
    if index % check_interval == 0:
        print('#', end='', flush=True)
    visited = []
    c = next_complex()
    z = (0,0)
    for _ in range(max_iter):
        z = add(mult(z, z), c)
        if mag2(z) > 4:
            return visited
        elif in_bounds(bounds, z):
            visited.append(point_to_bin(bounds, height, width, z))
    return []

def run(index):
    bins = [[0 for y in range(height)] for x in range(width)]
    for i in range(samples):
        points = sample(index * samples + i)
        for point in points:
            x, y = point
            bins[x][y] += 1
#    print('Run {} out of {} completed'.format(index + 1, runs))
    return bins

def create_image(bins):
    max_visits = max(map(max, bins))
    
    bitmap = Image.new('RGB', (width, height), "black")
    pixels = bitmap.load()
    
    for x in range(width):
        for y in range(height):
            level = bins[x][y] * 255 // max_visits
            pixels[x,y] = (level, level, level)
            
    return bitmap

if __name__ == '__main__':
    print('Sampling...')
    print('0123456789' * 10 + '0')
    pool = Pool(processes=threads)
    binslist = pool.map(run, range(runs))
    
    print('\nCreating Image...')
    bins = [[0 for y in range(height)] for x in range(width)]
    for x in range(width):
        for y in range(height):
            s = 0
            for b in binslist:
                s += b[x][y]
            bins[x][y] = s
    
    bitmap = create_image(bins)
            
    bitmap.save('images/buddhabrot.png', 'PNG')
    bitmap.show()