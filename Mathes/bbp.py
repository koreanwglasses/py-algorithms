from multiprocessing import Process

def modexp(b, e, m):
    if m == 1:
        return 0
    result = 1
    b = b % m
    while e > 0:
        if (e % 2) == 1:
            result = (result * b) % m
        e = e / 2
        b = (b * b) % m
    return result

def bbp(n):
    s1 = 0
    s2 = 0
    s3 = 0
    s4 = 0
    for k in xrange(0, n):
        s1 += modexp(16, n-k, 8*k+1) / (8 * k + 1.0)
        s1 += modexp(16, n-k, 8*k+4) / (8 * k + 4.0)
        s1 += modexp(16, n-k, 8*k+5) / (8 * k + 5.0)
        s1 += modexp(16, n-k, 8*k+6) / (8 * k + 6.0)
    return int(((4 * s1 - 2*s2 - s3 - s4) % 1)* 16)

def bbp_process(step, offset):
    return 0

print [bbp(n) for n in range(10)]