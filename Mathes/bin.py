import time

def f(x):
    return '{0:b}'.format(x).replace('0', '  ').replace('1', '██')[::-1]

i = 0
while True:
    print(f(i))
    time.sleep(.03)
    i = i + 1
