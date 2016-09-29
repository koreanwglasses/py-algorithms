from backtracking2 import BacktrackSolve
import time
import random

size = 10

board = [
    "23 3  2 3 ",
    "2 2   11 2",
    "2   23 2  ",
    "  21 1 11 ",
    "11 11  1  ",
    "2 20 20133",
    "21 2222  1",
    " 2  21111 ",
    " 1    2  3",
    " 2  3     "
]

def parse(char):
    if char == " ":
        return -1
    else:
        return int(char)

board = [[parse(char) for char in list(row)] for row in board]

# board = [
#     [ 3,-1, 3, 2,-1],
#     [-1, 2,-1,-1, 2],
#     [-1, 3,-1, 3, 0],
#     [-1,-1, 1, 2,-1],
#     [-1, 2, 2, 2,-1]
# ]

known = []
known_false = []

done = False

def fill_test(link, lack):
    if len(link) < 4:
        return True
    queue = [link[-1]]
    visited = []

    unvisited = lack[:]
    unvisited.append([0, [link[0]]])

    while len(queue) > 0:
        point = queue.pop(0)

        for i in range(len(unvisited) - 1, -1, -1):
            count, verts = unvisited[i]
            if point in verts:
                verts.remove(point)
                if len(verts) <= count:
                    del unvisited[i]
        if len(unvisited) == 0:
            return True
        
        next = free_neighbors(point, link + visited)
        visited.extend(next)
        queue.extend(next)
    return False

def free_neighbors(point, link):
    x, y = point
    neighbors = []

    if x + 1 < size + 1:
        neighbors.append((x + 1, y))
    if x - 1 > -1:
        neighbors.append((x - 1, y))
    if y + 1 < size + 1:
        neighbors.append((x, y + 1))
    if y - 1 > -1:
        neighbors.append((x, y - 1))
    
    if len(link) < 4:
        return list(set(neighbors) - set(link))
    else:
        return list(set(neighbors) - set(link[1:]))

def side_faces(link):
    x1, y1 = link[-1]
    x2, y2 = link[-2]

    faces = []
    if y1 == y2:
        x = min(x1, x2)
        if y1 - 1> -1:
            faces.append((x, y1 - 1))
        if y1 < size:
            faces.append((x, y1))
    else:
        y = min(y1, y2)        
        if x1 - 1 > -1:
            faces.append((x1 - 1, y))
        if x1 < size:
            faces.append((x1, y))     
    return faces   

def is_edge_in_path(link, v1, v2):
    if v1 not in link or v2 not in link:
        return False

    i1 = link.index(v1)
    i2 = link.index(v2)

    return abs(i1 - i2) == 1 or (i1 == 0 and i2 == len(link) - 2) or (i2 == 0 and i1 == len(link) - 2)

def vertices(face):
    x, y = face
    return [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]

old_link_length = 100
memoize_edges = {}
def edges(link, face):
    global old_link_length
    global memoize_edges

    if len(link) < old_link_length:
        memoize_edges = {}
    elif len(link) > 1:
        for side in side_faces(link):
            if face in memoize_edges:
                del memoize_edges[face]
        
        if face in memoize_edges:
            old_link_length = len(link)
            return memoize_edges[face]
    
    old_link_length = len(link)

    v = vertices(face)
    count = 0

    if is_edge_in_path(link, v[0], v[1]):
        count = count + 1
    if is_edge_in_path(link, v[1], v[2]):
        count = count + 1
    if is_edge_in_path(link, v[2], v[3]):
        count = count + 1
    if is_edge_in_path(link, v[3], v[0]):
        count = count + 1

    memoize_edges[face] = count

    return count

def is_known(point, link):
    for v1, v2 in known:
        if v1 == point and v2 not in link:
            return v2
        if v2 == point and v1 not in link:
            return v1
    return False

def is_known_false(link):
    if len(link) < 2:
        return True
    for v1, v2 in known_false:
        if (link[-1] == v1 and link[-2] == v2) or (link[-1] == v2 and link[-2] == v1):
            return False
    return True

def lackeys(link):
    v = []
    incomplete = False
    for i in range(size):
        for j in range(size):   
            if edges(link, (j, i)) < board[i][j]:
                v.append((3 + edges(link, (j, i)) - board[i][j], vertices((j, i))))
    return v

counter = 0
def get_candidates(link):
    global counter
    # if counter == 0:
    #     counter = 1
    #     print to_string(link)

    # Debug
    # counter += 1
    # if counter == 10000:
    #      counter = 0
    #      print to_string(link)
    #      time.sleep(.1)

    # print to_string(link)
    # time.sleep(.1)

    # Excluded Edges
    if not is_known_false(link):
        return []

    # Known Edges
    result = is_known(link[-1], link)
    if result != False:
        return [result]

    # Too many edges
    if len(link) > 1:
        for face in side_faces(link):
            x, y = face
            if board[y][x] > -1 and edges(link, face) > board[y][x]:
                return []
    
    # Too few
    lack = lackeys(link)

    if len(link) > 3 and link[0] == link[-1] and len(lack) == 0:
        global done
        done = True
        return []

    # Blocked off
    if not fill_test(link, lack):
        return []

    # Return
    candidates = free_neighbors(link[-1], link)
    random.shuffle(candidates)
    return candidates

def to_string(link):
    matrix = [[' ' for i in range(2 * size + 1)] for j in range(2 * size + 1)]
    for i in range(size):
        for j in range(size):
            if board[i][j] > -1:
                matrix[i * 2 + 1][j * 2 + 1] = str(board[i][j])

    for v1, v2 in known:
        x1, y1 = v1
        x2, y2 = v2

        matrix[y1 * 2][x1 * 2] = '+'
        matrix[y2 * 2][x2 * 2] = '+'
        if y1 == y2:
            matrix[y1 + y2][x1 + x2] = '~'    
        else:
            matrix[y1 + y2][x1 + x2] = ':'
    
    if not done:
        for v1, v2 in known_false:
            x1, y1 = v1
            x2, y2 = v2

            matrix[y1 + y2][x1 + x2] = 'x'

    for i in range(len(link) - 1):
        x1, y1 = link[i]
        x2, y2 = link[i + 1]

        matrix[y1 * 2][x1 * 2] = '+'
        if y1 == y2:
            matrix[y1 + y2][x1 + x2] = '-'    
        else:
            matrix[y1 + y2][x1 + x2] = '|'
    x, y = link[-1]
    matrix[y * 2][x * 2] = '+'

    return '\n'.join([''.join(row) for row in matrix])

def check(link):
    return done

# Pattern Matching

# 3 in corner
if board[0][0] == 3:
    known.append(((0,0),(1,0)))
    known.append(((0,0),(0,1)))

if board[0][size-1] == 3:
    known.append(((size,0),(size - 1,0)))
    known.append(((size,0),(size,1)))

if board[size - 1][0] == 3:
    known.append(((0,size),(0,size - 1)))
    known.append(((0,size),(1,size)))

if board[size - 1][size - 1] == 3:
    known.append(((size,size),(size,size - 1)))
    known.append(((size,size),(size -1,size)))

# One in corner

if board[0][0] == 1:
    known_false.append(((0,0),(1,0)))
    known_false.append(((0,0),(0,1)))

if board[0][size-1] == 1:
    known_false.append(((size,0),(size - 1,0)))
    known_false.append(((size,0),(size,1)))

if board[size - 1][0] == 1:
    known_false.append(((0,size),(0,size - 1)))
    known_false.append(((0,size),(1,size)))

if board[size - 1][size - 1] == 1:
    known_false.append(((size,size),(size,size - 1)))
    known_false.append(((size,size),(size -1,size)))

for i in range(size):
    for j in range(size):
        if board[i][j] == 3:
            # 3 in a row
            if i + 1 < size and board[i + 1][j] == 3:
                known.append(((j, i), (j + 1, i)))
                known.append(((j, i + 1), (j + 1, i + 1)))
                known.append(((j, i + 2), (j + 1, i + 2)))

                if j - 1 > -1:
                    known_false.append(((j - 1, i + 1), (j, i + 1)))
                if j + 2 < size + 1:
                    known_false.append(((j + 1, i + 1), (j + 2, i + 1)))
            if j + 1 < size and board[i][j + 1] == 3:       
                known.append(((j, i), (j, i + 1)))
                known.append(((j + 1, i), (j + 1, i + 1)))
                known.append(((j + 2, i), (j + 2, i + 1)))
                
                if i - 1 > -1:
                    known_false.append(((j + 1, i - 1), (j + 1, i)))
                if i + 2 < size + 1:
                    known_false.append(((j + 1, i + 1), (j + 1, i + 2)))

known = list(set(known))
known_false = list(set(known_false))

solution = BacktrackSolve([(0, 0), (0, 1), (1, 0), (1, 1), (2, 0)], get_candidates, check)
print(to_string(solution))