from backtracking2 import BacktrackSolve2

nmap = [(1,1,2,3),(0,0,2,3),(0,1,3),(0,1,2)]
start = 2

def edges_from_nmap(nmap):
    edges = []
    for v1 in range(len(nmap)):
        for v2 in nmap[v1]: 
            edges.append((v1, v2))

    return edges

def transpose(edge):
    return (edge[1], edge[0])

def remove_edge(edges, edge):
    new_edges = list(edges)
    i1 = new_edges.index(edge)
    del new_edges[i1]

    i2 = new_edges.index(transpose(edge))
    del new_edges[i2]

    return new_edges

def is_edge_available(edges, edge):
    return edge in edges and transpose(edge) in edges

def available_neighbors(edges, vertex):
    neighbors = nmap[vertex]
    candidates = []
    for v2 in neighbors:
        if is_edge_available(edges, (vertex, v2)):
            candidates.append((vertex,v2))
    return candidates

def get_candidates(state):
    edges, path = state

    if len(edges) == 0:
        return True

    candidates = []
    for edge in available_neighbors(edges, path[-1]):
        candidates.append((remove_edge(edges, edge), path + [edge[1]]))

    return candidates

print BacktrackSolve2([(edges_from_nmap(nmap), [start])], get_candidates)[1]