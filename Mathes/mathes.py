import gmpy2
from gmpy2 import mpz

## ---- List functions ---- ##

def combinations_lists(lists, y):
    comb = [i + [j] for i in lists for j in y];
    return comb

def combinations_2(x, y):
    comb = [[i,j] for i in x for j in y] 
    return comb

def combinations(lists):
    if len(lists) is 1:
        return lists[0]
    
    comb = combinations_2(lists[0], lists[1])
    if len(lists) is 2:
        return comb
    
    for i in range(2, len(lists)):
        comb = combinations_lists(comb, lists[i])
    return comb

def product(x):
    return reduce(lambda y,z: y * z, x)

## ---- Prime numbers and factorization ---- ##
def prime(n):
    p = 1
    for _ in xrange(n):
        p = gmpy2.next_prime(p)
    return p
    
def prime_factors(n):
    n = mpz(n)

    factors = []
    exponents = []
    
    p = mpz(2)
    e = 0
    
    while n != 1: 
        if n % p == 0:
            n = n // p
            e = e + 1
        else:
            if e != 0:
                factors.append(p)
                exponents.append(e)
                
            if gmpy2.is_prime(n):
                p = n
            else:
                p = gmpy2.next_prime(p)
            e = 0

    if e is not 0:
        factors.append(p)
        exponents.append(e)
        
    return factors, exponents

def count_factors(n):
    f, e = prime_factors(n)
    return product([x + 1 for x in e])

def count_uq_prime_factors(n):
    f, e = prime_factors(n)
    return len(f)

def factors(n):
    if n is 1:
        return [1]
    
    pfac, exp = prime_factors(n)
    
    if len(pfac) is 1:
        return [pfac[0] ** x for x in range (exp[0] + 1)]

    pfacpows = [[pfac[i] ** x for x in range(exp[i] + 1)] for i in range(len(pfac))]
    
    combs = combinations(pfacpows)
    factors = [product(x) for x in combs]

    return sorted(factors)

## ---- Number theory ---- ##

partitions_memoize = {}

def partitions_p(n, m):
    if m > n:
        return partitions_p(n, n)
    if n is 0 or m is 1:
        return 1
    p = sum(map(lambda k: partitions_p(n - k, k), range(1, m + 1)))
    return p

def partitions(n):
    p = partitions_p(n, n)
    
    return p

def collatz_trail_iterate(c):
    if gmpy2.is_even(c):
        return gmpy2.f_div_2exp(c,1)
    else:
        return c * 3 + 1

def collatz_trail(n):
    seq = [n]
    while True:
        n = collatz_trail_iterate(n)
        if n is 1:
            return seq
        seq.append(int(n))

def aliquot(n, maxiter = 20):
    seq = [n]
    itr = 0
    while itr < maxiter:            
        if n is 0:
            break
            
        n = sum(factors(n)) - n
    
        if n in seq:
            seq.append(n)
            return seq
    
        seq.append(n)
        
        itr = itr + 1
    
    return seq

# ---- Group Theory ---- #

def mod_log(a, b, n):
    return [e for e in range(n) if (a ** e) % n == b]

if __name__ == '__main__':
    print(mod_log(4, 6, 19))