def recomb(part):                
    part, ones = part
    nextparts = []
    if len(part) > 0:
        n = part[-1]
    else:
        n = 2
    while True:
        if ones >= n:
            newpart = list(part)
            newpart.append(n)
            
            nextparts.append((newpart, ones - n))
            
            n = n + 1
        else:
            break
    return nextparts

def printpart(part):
    part = list(reversed(part[0])) + [1 for _ in range(part[1])]
    print(' + '.join(map(str,part)))

n = int(input())

print()
q = [([], n)]
while len(q) > 0:
    p = q.pop()
    q += reversed(recomb(p))
    printpart(p)