import matplotlib.pyplot as plt

def step_to_iter(x):
    a = 0
    for _ in range(x):
        a = 2 * a + 1
    return a

steps = step_to_iter(int(input()))

x = [0, 1]
y = [0, 0]

directions = [(1, 0), (0, -1), (-1, 0), (0, 1)]
direction_i = 0
n = 0

plt.show()
while True:
    if n >= steps:
        break
    
    n = n + 1
    turn_left = (((n & -n) << 1) & n) != 0
    
    if turn_left:
        direction_i = (direction_i - 1) % 4
    else:
        direction_i = (direction_i + 1) % 4
        
    dx, dy = directions[direction_i]
    
    x.append(x[-1] + dx)
    y.append(y[-1] + dy)
#    
#    plt.plot(x[-2:], y[-2:], 'r-')
#    plt.axis([min(x) - 10, max(x) + 10, min(y) - 10, max(y) + 10])
#    plt.pause(.01)
#    plt.clf()

print('Done!')
plt.plot(x, y, 'r-')
plt.axis([min(x) - 10, max(x) + 10, min(y) - 10, max(y) + 10])
plt.show()