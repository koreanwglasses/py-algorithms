## functions ##
def recomb(part):            
    part, ones = part # each partitions consists of 1s, and numbers other than 1
    nextparts = []    # init an array of new partitions
                     
                      # n will be the number you collapse ones into. ie if n = 2 and p = 1 + 1 + 1, a new partition would be 2 + 1.

    if len(part) > 0: # As long as the numbers arent just ones, let n be the last 
                      # number in the partition. ie, if p = 1 + 1 + 2 + 3, then n = 3
        n = part[-1]
    else:
        n = 2         # otherwise let n be two.

    while True: 
        if ones >= n:                             # as long as you have enough ones to collapse...
            newpart = list(part)
            newpart.append(n)
            
            nextparts.append((newpart, ones - n)) # collapse them
            
            n = n + 1
        else:
            break
    return nextparts # return all the new partitions

def printpart(part):
    part = list(reversed(part[0])) + [1 for _ in range(part[1])] # messy one liner that does exactly what its supposed to so does it really matter?
                                                                 # of course it does
    print(' + '.join(map(str,part)))

## Main Program ##
n = int(input())         # take the input

print                    # print a new line
q = [([], n)]            # create a queue of partitions
while len(q) > 0:        # while the queue is not empty
    p = q.pop()              # pop a partition from q
    q += reversed(recomb(p)) # use this partition to generate more partitions and add them to the queue
    printpart(p)             # print the partition