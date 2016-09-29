import gmpy2
from gmpy2 import mpz
from gmpy2 import xmpz
from multiprocessing import Process
from multiprocessing import Value
import time

def iterate(c):
    if gmpy2.is_even(c):
        return c >> 1
    else:
        return (c << 1) + c + 1

def check(n):
    c = n
    seq = [c]
    while True:    
        c = iterate(c)
        
        if c < n:
            return True
        if c in seq:
            return False
        
        seq.append(c)

def sweep(start, threadID, stride, update_interval): 
    print 'Starting Thread ' + str(threadID)
    
    n = mpz(start)
    counter = 0
    while True:
        if not check(n):
            break
        n = n + (2 * stride) 

        counter = counter + 1
        if counter >= update_interval:
            print n
            counter = 0

    print '\n'
    print 'Woah'
    print n
    print '\n'

def all_alive(ps):
    for p in ps:
        if not p.is_alive():
            return False
    return True

if __name__ == '__main__':
    n = raw_input().split() # 1152921534850000005 1152921534850000007 1152921534850000003 1152921534850000001 1152921534850000009

    ps = []
    for i in xrange(len(n)):
        p = Process(target=sweep, args=(n[i],i,len(n),10000000))
        ps.append(p)
        p.start()

    while True:
        if not all_alive(ps):      
            for p in ps:
                if p.is_alive():
                    p.terminate()
            break
        time.sleep(10)