from backtracking2 import BacktrackSolve2
import time
import random

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

def vertices(face):
    x, y = face
    return [(x, y), (x + 1, y), (x + 1, y + 1), (x, y + 1)]

def edges(link, face):
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

    return count

def edge_between(face1, face2):
    x1, y1 = face1
    x2, y2 = face2
    if x1 == x2:
        return ((x1, max(y1, y2)), (x1 + 1, max(y1, y2)))
    else:
        return ((max(x1, x2), y1), (max(x1, x2), y1 + 1))

def update(link, side_faces, edge_counts, parity):
    for face in side_faces:
        x, y = face
        parity[y][x] = -1

    for face in side_faces:
        x, y = face
        edge_counts[y][x] = edges(link, face)
        
        free, blocked = adj_faces(link, face)
        p = -1
        for j, i in blocked:
            if j < 0 or j >= size or i < 0 or i >= size:
                p = 1
                break
            elif parity[i][j] == 0:
                p = 1
                break
            elif parity[i][j] == 1:
                p = 0
                break
        parity[y][x] = p
    return True

def over(side_faces, edge_counts):
    for face in side_faces:
        x, y = face
        if board[y][x] > -1 and edge_counts[y][x] > board[y][x]:
            return False
    return True

def under(edge_counts):
    v = []
    for i in range(size):
        for j in range(size):   
            if edge_counts[i][j] < board[i][j]:
                v.append((3 + edge_counts[i][j] - board[i][j], vertices((j, i))))
    return v

def empty_array(value, size):
    return [[value for i in range(size)] for j in range(size)]

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

def adj_faces(link, face):
    v = vertices(face)
    x, y = face

    free = []
    blocked = []
    if is_edge_in_path(link, v[0], v[1]):
        blocked.append((x, y - 1))
    else:
        free.append((x, y - 1))
    if is_edge_in_path(link, v[1], v[2]):
        blocked.append((x + 1, y))
    else:
        free.append((x + 1, y))
    if is_edge_in_path(link, v[2], v[3]):
        blocked.append((x, y + 1))
    else:
        free.append((x, y + 1))
    if is_edge_in_path(link, v[3], v[0]):
        blocked.append((x - 1, y))
    else:
        free.append((x - 1, y))

    return (free, blocked)

def get_parity(face, parity):
    x, y = face
    if x < 0 or x >= size or y < 0 or y >= size:
        return 0
    else:
        return parity[y][x]

def parity_pass_0(link, parity):
    for i in range(size):
        for j in range(size):
            if parity[i][j] == -1:
                face = (j,i)
                free, blocked = adj_faces(link, face)
                p = -1
                for face in blocked:
                    if get_parity(face, parity) == 0:
                        p = 1
                        break
                    elif get_parity(face, parity) == 1:
                        p = 0
                        break
                parity[i][j] = p

def parity_pass_1(link, parity, known_edges):
    for i in range(size):
        for j in range(size):
            if board[i][j] > -1 and (parity[i][j] > -1 or (j, i) in side_faces(link)):
                free, blocked = adj_faces(link, (j, i))
                adj = free + blocked

                inside = []
                outside = []

                for face in adj:
                    if get_parity(face, parity) == 0:
                        outside.append(face)
                    elif get_parity(face, parity) == 1:
                        inside.append(face)
                
                if board[i][j] == 0:
                    val = -1
                    for face in adj:
                        if get_parity(face, parity) > -1:
                            val = get_parity(face, parity)
                            break
                    if val > -1:
                        for x, y in adj:
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = val
                if board[i][j] == 1:
                    if len(outside) == 1 and parity[i][j] == 1:
                        known_edges.append(edge_between((j, i), outside[0]))
                        for x, y in set(adj) - set(outside):
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = 1
                    if len(inside) == 1 and parity[i][j] == 0:
                        known_edges.append(edge_between((j, i), inside[0]))
                        for x, y in set(adj) - set(inside):
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = 0

                    if len(inside) == 3:
                        face = list(set(adj) - set(inside))[0];
                        known_edges.append(edge_between((j, i), face))
                        
                        x, y = face
                        parity[i][j] = 1
                        if x >= 0 and x < size and y >= 0 and y < size:
                            parity[y][x] = 0
                    if len(outside) == 3:
                        face = list(set(adj) - set(outside))[0];
                        known_edges.append(edge_between((j, i), face))

                        x, y = face
                        parity[i][j] = 0
                        if x >= 0 and x < size and y >= 0 and y < size:
                            parity[y][x] = 1
                if board[i][j] == 2:
                    if len(outside) == 2 and parity[i][j] == 0:
                        for face in set(adj) - set(outside):
                            known_edges.append(edge_between((j, i), face))

                            x, y = face
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = 1
                    if len(outside) == 2 and parity[i][j] == 1:
                        for face in outside:
                            known_edges.append(edge_between((j, i), face))

                        for x, y in set(adj) - set(outside):
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = 1

                    if len(inside) == 2 and parity[i][j] == 1:
                        for face in set(adj) - set(inside):
                            known_edges.append(edge_between((j, i), face))

                            x, y = face
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = 0
                    if len(inside) == 2 and parity[i][j] == 0:
                        for face in inside:
                            known_edges.append(edge_between((j, i), face))

                        for x, y in set(adj) - set(inside):
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = 0
                if board[i][j] == 3:
                    if len(outside) == 1 and parity[i][j] == 0:
                        for face in set(adj) - set(outside):
                            known_edges.append(edge_between((j, i), face))

                            x, y = face
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = 1
                    if len(inside) == 1 and parity[i][j] == 1:
                        for face in set(adj) - set(inside):
                            known_edges.append(edge_between((j, i), face))

                            x, y = face
                            if x >= 0 and x < size and y >= 0 and y < size:
                                parity[y][x] = 0

                    if len(inside) == 3:
                        for face in inside:
                            known_edges.append(edge_between((j, i), face))               
                        parity[i][j] = 0

                        face = list(set(adj) - set(inside))[0]
                        x, y = face
                        if x >= 0 and x < size and y >= 0 and y < size:
                            parity[y][x] = 0
                    if len(outside) == 3:
                        for face in outside:
                            known_edges.append(edge_between((j, i), face))               
                        parity[i][j] = 1

                        face = list(set(adj) - set(outside))[0]
                        x, y = face
                        if x >= 0 and x < size and y >= 0 and y < size:
                            parity[y][x] = 1

def check_known(link, known_edges):
    if len(link) < 3 or len(known_edges) == 0:
        return True
    for v1, v2 in known_edges:
        if (v1 in link[1:-1] and not v2 in link) or (v2 in link[1:-1] and not v1 in link):
            return False
    return True

def follow_known(link, known_edges):
    for v1, v2 in known_edges:
        if link[-1] == v1 and link[-2] != v2:
            return v2
        elif link[-1] == v2 and link[-2] != v1:
            return v1
    return False

def get_candidates(solution):
    link, edge_counts, parity, known_edges = solution

    if len(link) > 1:
        faces = side_faces(link)
        update(link, faces, edge_counts, parity)
        parity_pass_0(link, parity)
        parity_pass_1(link, parity, known_edges)

        # print to_string(solution)
        # print
        # time.sleep(.1)

        if link[0] == link[-1]:
            sub = under(edge_counts)
            if over(faces, edge_counts) and fill_test(link, sub):
                return True

        known_edges = list(set(known_edges))
        if check_known(link, known_edges) == False:
            return []

        known_result = follow_known(link, known_edges)
        if known_result != False:      
            newlink = link[:]
            newlink.append(known_result)

            newedge = [row[:] for row in edge_counts]
            newparity = [row[:] for row in parity]
            new_known_edges = known_edges[:]

            return [[newlink, newedge, newparity, new_known_edges]]

        if not over(faces, edge_counts):
            return []

        sub = under(edge_counts)
        if not fill_test(link, sub):
            return []

        if link[0] == link[-1]:
            return True

    candidates = []
    for neighbor in free_neighbors(link[-1], link):
        newlink = link[:]
        newlink.append(neighbor)

        newedge = [row[:] for row in edge_counts]
        newparity = [row[:] for row in parity]
        new_known_edges = known_edges[:]

        candidates.append([newlink, newedge, newparity, new_known_edges])
    return candidates

def to_string(solution):
    link, edge_counts, parity, known_edges = solution

    matrix = [[' ' for i in range(2 * size + 1)] for j in range(2 * size + 1)]

    for row in matrix:
        row[1::2] = ['  ' for _ in range(size)]

    for i in range(size):
        for j in range(size):
            shade = ' '
            if parity[i][j] == 0:
                shade = u'\u2591'
            elif parity[i][j] == 1:
                shade = u'\u2593'
            elif parity[i][j] == -2:
                shade = '#'

            if board[i][j] > -1:
                matrix[i * 2 + 1][j * 2 + 1] = str(board[i][j]) + shade 
            else:
                matrix[i * 2 + 1][j * 2 + 1] = shade + shade

    for i in range(len(link) - 1):
        x1, y1 = link[i]
        x2, y2 = link[i + 1]

        matrix[y1 * 2][x1 * 2] = '+'
        if y1 == y2:
            matrix[y1 + y2][x1 + x2] = '--'    
        else:
            matrix[y1 + y2][x1 + x2] = '|'
    x, y = link[-1]
    matrix[y * 2][x * 2] = 'x'

    for v1, v2 in known_edges:
        x1, y1 = v1
        x2, y2 = v2

        matrix[y1 * 2][x1 * 2] = '+'
        matrix[y2 * 2][x2 * 2] = '+'
        if y1 == y2:
            matrix[y1 + y2][x1 + x2] = '--'    
        else:
            matrix[y1 + y2][x1 + x2] = '|'

    return '\n'.join([''.join(row) for row in matrix])

# size = 5
# board = [
#     [ 3,-1, 3, 2,-1],
#     [-1, 2,-1,-1, 2],
#     [-1, 3,-1, 3, 0],
#     [-1,-1, 1, 2,-1],
#     [-1, 2, 2, 2,-1]
# ]

# Test Case

size = 10
board = [
    "3   322211",
    "  12    33",
    " 32  32  2",
    "  3 1  3 3",
    "  1    122",
    "  3      2",
    " 1    1231",
    " 2       2",
    "22   22221",
    "3332 23222"
]

def parse(char):
    if char == " ":
        return -1
    else:
        return int(char)

board = [[parse(char) for char in list(row)] for row in board]

# End Test Case

start = time.time()

initial = [[(0,0)], empty_array(0, size), empty_array(-1, size), []]

solution = BacktrackSolve2([initial], get_candidates)

print to_string(solution)
print "Solved in " + str(time.time() - start)