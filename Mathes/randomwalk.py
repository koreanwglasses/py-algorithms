from backtracking import Backtrack
import matplotlib.pyplot as plt
import time
import math
import random

steps = int(input())

def fill_test(path, limit):
    queue = [path[-1]]
    visited = list(path)
    count = 0
    while len(queue) > 0:
#        xs, ys = zip(*queue)
#        plt.plot(xs, ys, 'go')
        
        if count > limit:
            return True
        count = count + 1
        
        point = queue.pop(0)
        neighbors = get_free_neighbors(visited, point)
        
        visited.extend(neighbors)
        queue.extend(neighbors)
    return False

card_dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
card_dir_inv = {card_dir[0]: 0, card_dir[1]: 1, card_dir[2]: 2, card_dir[3]: 3}

def cw(direction):
    index = (card_dir_inv[direction] - 1) % 4
    return card_dir[index]

def ccw(direction):
    index = (card_dir_inv[direction] + 1) % 4
    return card_dir[index]

def ang(dir_a, dir_b):
    ind_a = card_dir_inv[dir_a]
    ind_b = card_dir_inv[dir_b]
    
    ang = ind_b - ind_a
    if ang == 3:
        return -1
    if ang == -3:
        return 1
    return ang

def sub(a, b):
    return (a[0] - b[0], a[1] - b[1])

def add(a, b):
    return (a[0] + b[0], a[1] + b[1])

def turning_no(path, index):
    if index < 0:
        index = index + len(path)
    
    t = 0
    last_dir = (sub(path[1], path[0]))
    for i in range(1, index):
        new_dir = sub(path[i + 1], path[i])
        t = t + ang(last_dir, new_dir)
        last_dir = new_dir
    return t

def loop_test(path):
    if len(path) < 3:
        return True
    
    forward = sub(path[-1], path[-2])
    
    right = add(path[-1], cw(forward))
    left = add(path[-1], ccw(forward))
    
    right_back = sub(right, forward)
    left_back = sub(left, forward)
    
    right_tail = sub(right_back, forward)
    left_tail = sub(left_back, forward)
    
    t_last = turning_no(path, -1)
    
    if right in path:
        index = path.index(right)
        t_n1 = turning_no(path, index)
        t_n2 = turning_no(path, index + 1)
        if t_last == t_n1 + 4 or t_last == t_n1 + 6 or t_last == t_n2 + 4 or t_last == t_n2 + 6:
            return False
    if left in path:
        index = path.index(left)
        t_n1 = turning_no(path, index)
        t_n2 = turning_no(path, index + 1)
        if t_last == t_n1 - 4 or t_last == t_n1 - 6 or t_last == t_n2 - 4 or t_last == t_n2 - 6:
            return False
        
    if right_back in path:
        index = path.index(right_back)
        if path[index + 1] != path[-2]:
            t_n = turning_no(path, index)
            if t_last == t_n + 4 or t_last == t_n + 6:
                return False
    if left_back in path:
        index = path.index(left_back)
        if path[index + 1] != path[-2]:
            t_n = turning_no(path, index)
            if t_last == t_n - 4 or t_last == t_n - 6:
                return False
            
    if right_tail in path:
        index = path.index(right_tail)
        if path[index + 2] != path[-2]:
            t_n = turning_no(path, index)
            if t_last == t_n + 4 or t_last == t_n + 6:
                return False
    if left_tail in path:
        index = path.index(left_tail)
        if path[index + 2] != path[-2]:
            t_n = turning_no(path, index)
            if t_last == t_n - 4 or t_last == t_n - 6:
                return False
            
    return True
        
def get_free_neighbors(path, point):
    neighbors = []

    x, y = point
    
    if (x + 1, y) not in path:
        neighbors.append((x + 1, y))
    if (x - 1, y) not in path:       
        neighbors.append((x - 1, y))
    if (x, y + 1) not in path:   
        neighbors.append((x, y + 1))
    if (x, y - 1) not in path:
        neighbors.append((x, y - 1))
        
    return neighbors
    
def get_candidates(path):
    draw_path(path)
    plt.clf()
    
    neighbors = get_free_neighbors(path, path[-1])
    if neighbors == []:
        return []
    
    area = steps - len(path)
    if not loop_test(path):
        if not fill_test(path, area):
            return []
    
    candidates = []    
    
    for neighbor in neighbors:
        candidate = list(path)
        candidate.append(neighbor)
        candidates.append(candidate)
    
    random.shuffle(candidates)
    return candidates

def draw_path(path):
    xs, ys = zip(*path)
    
    plt.plot(xs[0], ys[0], 'go')
    plt.plot(xs[-1], ys[-1], 'bo')
    
    plt.plot(xs, ys, 'r-')
    plt.axis([min(xs) - 20, max(xs) + 20, min(ys) - 20, max(ys) + 20])
    plt.pause(0.1)
    
solver = Backtrack(get_candidates)

plt.show()

solution = solver.solve([(0,0)], steps)

draw_path(solution)
plt.show()
    