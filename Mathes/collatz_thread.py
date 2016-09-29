import gmpy2
from gmpy2 import mpz
import threading

class collatz (threading.Thread):
    def __init__(self, start, offset, stride, update_interval=1000000):
        threading.Thread.__init__(self)
        self.start = start
        self.offset = offset
        self.stride = stride
        self.update_interval = update_interval
        
    def run(self):
        print 'Starting Thread ' + str(self.offset)
        sweep(self.start, self.offset, self.stride, self.update_interval)
        print 'Exiting Thread ' + str(self.offset)

def set_exitflag(b):
    global exitflag
    exitflag = b

def iterate(c):
    if gmpy2.is_even(c):
        return gmpy2.f_div_2exp(c,1)
    else:
        return c * 3 + 1

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

exitflag = False
        
def sweep(start, offset, stride, update_interval): 
    n = mpz(start) + 2 * offset
    counter = 0
    while not exitflag:
        if not check(n):
            break
        n = n + (2 * stride) 

        counter = counter + 1
        if counter >= update_interval:
            print n
            counter = 0

    if not exitflag:
        set_exitflag(True)

        print '\n'
        print 'Woah'
        print n
        print '\n'

set_exitflag(False)        

n = raw_input()
thread_count = int(raw_input())

for i in xrange(thread_count):
    thread = collatz(n, i, thread_count)
    threading.Thread.start(thread)

raw_input()
set_exitflag(True)