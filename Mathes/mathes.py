import gmpy2
from gmpy2 import mpz
import numbers
import math

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

def continued_fraction(n, d):
    cf = []
    while d > 0:
        cf.append(n // d)
        n, d = d, n % d
    return cf

# ---- Approximations ---- #
def nint_simp(f, a, b, n):
    h = (b - a) / float(n)
    area = 0.5 * f(a) + 0.5 * f(b)
    for i in range(n):
        area += 2 * f(a + h*i + 0.5 * h)
    for i in range(n - 1):
        area += f(a + h * (i + 1))
    return area * h / 3

def nint_simp_inf(f, n):
    return nint_simp(lambda t: f(t / (1. - t**2)) * (1. + t**2) / (1 - t**2)**2, 2./n - 1, 1 - 2./n, n)

def nint2d_simp_inf(f, n):
    return nint_simp_inf(lambda y: nint_simp_inf(lambda x: f(x, y), n), n)

def sec_root(f, n=-1, e=1e-15, x_0=-.5, x_1=.75):
    x = [0, x_1, x_0]

    def sec_iter():
        print x
        x[0], x[1], x[2] = (x[2] * f(x[1]) - x[1] * f(x[2])) / (f(x[1]) - f(x[2])), x[0], x[1]

    if n <= 0:
        while abs(x[0] - x[1]) > e:
            sec_iter()
        return x[0]
    else:
        for _ in range(n):
            sec_iter()
            if abs(x[0] - x[1]) < e:
                break
        return x[0]

def bis_root(f, a, b, n=-1, e=1e-15, debug=False):
    x = [a, b, 0, -1]

    assert (f(a) > 0) != (f(b) > 0)
    falt0 = f(a) < 0

    def bis_iter():
        if debug:
            print x
        x[2] = (x[0] + x[1]) / 2.0
        x[3] = f(x[2])
        if x[3] == 0:
            return True
        elif x[3] > 0:
            if falt0:
                x[1] = x[2]
            else:
                x[0] = x[2]
            return False
        elif x[3] < 0:
            if falt0:
                x[0] = x[2]
            else:
                x[1] = x[2]
            return False

    if n <= 0:
        while abs(x[3]) > e:
            if bis_iter():
                return x[2]
        return x[2]
    else:
        for _ in range(n):
            if bis_iter():
                return x[2]
            if abs(x[3]) < e:
                break
        return x[2]

# ---- Statistics ---- #

def erf_precise(z, k=30):
    return nint_simp(lambda t: math.e**(-t**2 / 2.0), 0, z, k)

def qrt_precise(p, k=30):
    assert 0 <= p and p <= 1
    if p == 1:
        return float("inf")
    elif p == 0:
        return float("-inf")
    return bis_root(lambda z: 0.5 + erf_precise(z) / math.sqrt(2 * math.pi) - p, -10, 10)

erf_coeff = [ 1,
    .0705230784, .0422820123,
    .0092705272, .0001520143,
    .0002765672, .0000430638
]
def erf(z):
    x = abs(z) / math.sqrt(2)
    e = 1 - 1 / (sum(erf_coeff[n] * x**n for n in range(7))**16)
    if z > 0:
        return e * math.sqrt(math.pi/2)
    else:
        return -e * math.sqrt(math.pi/2)

erfinv_c = []
def erfinv(z):
    if len(erfinv_c) == 0:
        global erfinv_c
        n = [1, 1, 7, 127, 4369, 34807, 20036983, 2280356863, 49020204823, 65967241200001, 15773461423793767, 655889589032992201, 94020690191035873697, 655782249799531714375489, 44737200694996264619809969]
        d = [1, 1, 6, 90, 2520, 16200, 7484400, 681080400, 11675664000, 12504636144000, 2375880867360000, 78404068622880000, 8910391798788480000, 49229914688306352000000, 2658415393168543008000000]
        erfinv_c = [math.pi**k * n[k] * 2**-(2 * k + 1) / ((2 * k + 1) * d[k]) for k in range(15)]
    return 0.5 * math.sqrt(math.pi) * sum(z**(2 * k + 1) * erfinv_c[k] for k in range(15))

def qrt(p):
    assert 0 <= p and p <= 1
    if p == 1:
        return float("inf")
    elif p == 0:
        return float("-inf")

    return 2 * math.sqrt(2) * erfinv(2 * p - 1)

# ---- Group Theory ---- #

def mod_log(a, b, n):
    return [e for e in range(n) if (a ** e) % n == b]

# ---- Matrices ---- #
class Matrix:
    def __init__(self, data, width, height):
        self.data = data
        self.width = width
        self.height = height

    def __getitem__(self, key):
        return self.data[key]
    
    def __setitem__(self, key, value):
        self.data[key] = value

    def __radd__(self, lhs):
        if isinstance(lhs, numbers.Number):
            new_data = [[self.data[r][c] + lhs for c in range(self.width)] for r in range(self.height)]
            return Matrix(new_data, self.width, self.height)
    def __add__(self, rhs):
        assert self.height == rhs.height and self.width == rhs.width
        new_data = [[self.data[r][c] + rhs.data[r][c] for c in range(self.width)] for r in range(self.height)]
        return Matrix(new_data, self.width, self.height)

    def __sub__(self,rhs):
        assert self.height == rhs.height and self.width == rhs.width
        new_data = [[self.data[r][c] - rhs.data[r][c] for c in range(self.width)] for r in range(self.height)]
        return Matrix(new_data, self.width, self.height)

    def __rmul__(self, lhs):
        if isinstance(lhs, numbers.Number):
            return self.__mul__(lhs)
    def __mul__(self, rhs):
        if isinstance(rhs, numbers.Number):
            new_data = [[self.data[r][c] * rhs for c in range(self.width)] for r in range(self.height)]
            return Matrix(new_data, self.width, self.height)
        elif isinstance(rhs, Matrix):
            assert self.width == rhs.height
            new_data = [[sum(self.data[r][k] * rhs.data[k][c] for k in range(self.width)) for c in range(rhs.width)] for r in range(self.height)]
            return Matrix(new_data, rhs.width, self.height)

    def __str__(self):
        return '\n'.join([str(row) for row in self.data])

    def transpose(self):
        new_data = [[self.data[r][c] for r in range(self.height)] for c in range(self.width)]
        return Matrix(new_data, self.height, self.width)

    def minor(self, rex, cex):
        new_data = [[self.data[r][c] for c in range(self.width) if c != cex] for r in range(self.height) if r != rex]
        return Matrix(new_data, self.width - 1, self.height - 1)

    def det_naive(self):
        assert self.width == self.height
        if self.width == 2:
            return self.data[0][0] * self.data[1][1] - self.data[0][1] * self.data[1][0]
        else:
            return sum(self.data[0][c] * self.minor(0, c).det_naive() * (-1)**(c) for c in range(self.width))

if __name__ == '__main__':
    # i = Matrix([[1,0,0,0]], 4, 1)
    # j = Matrix([[0,1,0,0]], 4, 1)
    # k = Matrix([[0,0,1,0]], 4, 1) 
    # l = Matrix([[0,0,0,1]], 4, 1)

    # m1 = Matrix([[i,j,k,l],[1,2,3,4],[-3,-4,5,6],[5,6,7,8]], 4, 4)

    # print m1.det_naive()
    # print m1.det_naive() * Matrix([[1,2,3,4]],4, 1).transpose()

    import matplotlib.pyplot as plt
    import numpy as np

    f = np.vectorize(qrt)
    g = np.vectorize(qrt_precise)
    x = np.arange(0.01, 1, 0.01)

    plt.show()
    # plt.plot(x, f(x), 'r-')
    # plt.plot(x, g(x), 'g-')
    # plt.axis([0, 1, -2, 2])
    plt.plot(x, f(x) - g(x), 'b-')
    plt.axis([0, 1, -0.1, 0.1])
    plt.show()

    # import random
    # rand1 = [qrt(random.random()) for _ in range(1000)]
    # rand2 = [qrt_precise(random.random()) for _ in range(1000)]
    # rand3 = [random.gauss(0, 1) for _ in range(1000)]
    # f = open('images/normal.csv','w+')
    # f.write('\n'.join(['{},{},{}'.format(rand1[i], rand2[i], rand3[i]) for i in range(1000)]))