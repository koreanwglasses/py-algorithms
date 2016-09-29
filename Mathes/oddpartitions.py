def recomb(part):                # Recombine Ones
    part, ones = part            # Unpack Input
    nextparts = []               # Store next partitions
    if len(part) > 0:            # Start with last value
        n = part[-1]
    else:
        n = 3                    # Start with 3 if first
    while True:
        if ones >= n:            # Condense n ones if possible
            newpart = list(part)
            newpart.append(n)
            
            nextparts.append((newpart, ones - n))
            
            n = n + 2           # Increment n to next odd number
        else:
            break               # Otherwise return
    return nextparts

def printpart(part):            # Print each partition
    part = list(reversed(part[0])) + [1 for _ in range(part[1])]
    print(' + '.join(map(str,part)))

n = int(input())

print()
q = [([], n)]                   # Declare Queue
while len(q) > 0:               # While queue is not empty
    p = q.pop()
    q += reversed(recomb(p))    # Put recombinations on queu
    printpart(p)