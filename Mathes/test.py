# import matplotlib.pyplot as plt
# import gmpy2
# from gmpy2 import mpz

def m_bonacci_lst(n, m):
    last = [1 for _ in range(m)]
    for _ in range(n - m):
        new = sum(last)
        last.append(new)
        del last[0]
    return last

def m_bonacci(n, m):
    return m_bonacci_lst(n, m)[-1];

def m_bonacci_cnst(m, n=100):
    last = m_bonacci_lst(n, m);
    return last[-1] / last[-2];

# n, m = map(int, input().split());
# print(m_bonacci_cnst(m, n))

# xs = range(2, 13)
# ys = [m_bonacci_cnst(m) for m in xs]

# plt.show()
# plt.plot(xs,ys,'r-')
# plt.axis([min(xs), max(xs), min(ys), max(ys)])
# plt.show()

# pi = 1
# p = mpz(1)
# while True:
#     p = gmpy2.next_prime(p)
#     if p % 4 == 1:
#         pi *= 1 + 1 / float(p)
#     elif p % 4 == 3:
#         pi *= 1 - 1 / float(p)

#     print "{} {}".format(pi, p)

for a in range(2,1000):
    for b in range(2,1000):
        if (a * a + b * b) % (a * b + 1) == 0:
            print '{} {} {}'.format(a, b, int(((a * a + b * b) / (a * b + 1))**.5)) 