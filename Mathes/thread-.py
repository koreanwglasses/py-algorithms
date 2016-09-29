import math

fourthpi = 0

n = 1
add = True
while True:
    if add:
        fourthpi += 1 / n
    else:
        fourthpi -= 1 / n
    add = not add
    n += 2
    
    print('{0}: {1:15.15f}, {2:15.15f}'.format(n, 4 * fourthpi, abs(math.pi - 4 * fourthpi)))