import time
def iterate(n):
    n = n * 3 + 1
    while (n & 1) == 0:
        n = n >> 1
    return n

def form(n):
    out = "{0:b}".format(n)
    out = out.replace("0", "  ")
    out = out.replace("1", "██")
    return out[::-1]

while True:
    n = eval(input())
    while True:
        print(form(n))
        
        if n == 1:
            break
        
        n = iterate(n)
        
#        time.sleep(.1)