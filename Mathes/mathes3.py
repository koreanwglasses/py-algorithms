partitions_moize = {}

def partitions_p(n, m):
    if m > n:
        return partitions_p(n, n)
    if n is 0 or m is 1:
        return 1
    
    if partitions_moize.has_key((n, m)):
        return partitions_moize[n, m]
    
    p = sum(map(lambda k: partitions_p(n - k, k), range(1, m + 1)))
    
    partitions_moize[n, m] = p
    
    return p

def partitions(n):
    p = partitions_p(n, n)
    
    return p

def telephone(n):
    if n < 2:
        return 1
    a = 1
    b = 1
    for k in range(1, n):
        c = b + k * a
        a = b
        b = c
    return b

def matrix_mult(a, b):
    assert len(a[0]) == len(b)
    rows = range(len(a))
    cols = range(len(b[0]))
    prod = [[0 for i in cols] for j in rows]
    
    for r in rows:
        for c in cols:
            prod[r][c] = sum(map(lambda l, r: l * r, a[r], map(lambda i: b[i][c], rows)))
    
    return prod

def print_matrix(m):
    pad = len(str(max(map(max, m))))
    template = '{:>' + str(pad) + '}'
    strings = [map(lambda d: template.format(d), m[r]) for r in range(len(m))]
    print('\n'.join(map(lambda row: '[ ' + ' '.join(row) + ' ]', strings)))

fastmod_moize = {}
def gen_fastmod_graph(m, b):
    if (m, b) in fastmod_moize:
        return fastmod_moize[(m,b)]
    
    graph = {}
    for i in range(m):
        graph[(i * b) % m] = i
    
    if len(fastmod_moize) < 1000:
        fastmod_moize[(m,b)] = graph
    
    return graph

def fastmod(n, m):
    graph = gen_fastmod_graph(m,2)
    p = 0
    while n > 0:
        if n & 1:
            p = p - 1
            if p < 0:
                p += m
        p = graph[p]
        print('{:b}'.format(p))
        n = n >> 1
        
    if p == 0:
        return 0
    return 7 - p
    
if __name__ == '__main__':
    print(fastmod(13 * 23, 13) == 0)
    print()
    print(fastmod(1323, 13) == 0)