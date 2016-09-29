import gmpy2
from gmpy2 import mpz

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
        
n = mpz(1152921509495000001)
counter = 0
while True:
    if not check(n):
        break
    n = n + 2
    
    counter = counter + 1
    if counter >= 1000000:
        print n
        counter = 0

print '\n'
print 'Woah'
print n
raw_input()