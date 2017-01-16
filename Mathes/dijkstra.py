edges = [(0,1,1),(1,2,1),(0,3,3),(1,4,7),(2,5,3),(3,4,9),(4,5,2),(3,6,1),(4,7,10),(5,8,1),(6,7,2),(7,8,3)]

def reverse(edge):
    return (edge[1], edge[0], edge[2])

def strip(edge):
    return (edge[0], edge[1])

def nodes(edges):
    n = []
    for v1, v2, val in edges:
        n.append(v1)
        n.append(v2)
    return list(set(n))

def neighbors_v(v, edges):
    n = [v1 for v1, v2, val in edges if v2 == v] + [v2 for v1, v2, val in edges if v1 == v]
    return list(set(n))

def neighbors_e(v, edges):
    return [edge for edge in edges if (edge[0] == v) or (edge[1] == v)]

def edges_between(v1, v2, edges):
    e = [edge for edge in edges if ((v1, v2) == strip(edge)) or ((v1, v2) == strip(reverse(edge)))]
    return e

def dijkstra(start, end, edges):
    all_nodes = nodes(edges)
    unvisited = list(all_nodes)

    values = {}
    for node in all_nodes:
        values[node] = "inf"

    current = start
    values[current] = 0
    while True:
        unvisited.remove(current)
        
        for node in neighbors_v(current, edges):
            min_distance = min(val for v1, v2, val in edges_between(current, node, edges))
            new_value = values[current] + min_distance
            if values[node] == "inf" or new_value < values[node]:
                values[node] = new_value

        if end not in unvisited:
            break

        current = unvisited[0]
        for node in unvisited[1:]:
            if values[node] != "inf" and values[node] < values[current]:
                current = node

    return values[current]

print dijkstra(0,8,edges)