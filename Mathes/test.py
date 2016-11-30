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

import time

times_csv = ''

def test(a, b, c, n):
    return a * a * a + b * b * b + c * c * c == n

def sum_of_cubes(n):
    limit = 1
    while limit < 300:
        for a in [-limit, limit]:
            for b in range(-limit, limit + 1):
                for c in range(-limit, limit + 1):
                    if test(a, b, c, n):
                        return (a, b, c)
        for b in [-limit, limit]:
            for a in range(-limit, limit + 1):
                for c in range(-limit, limit + 1):
                    if test(a, b, c, n):
                        return (a, b, c)
        for c in [-limit, limit]:
            for a in range(-limit, limit + 1):
                for b in range(-limit, limit + 1):
                    if test(a, b, c, n):
                        return (a, b, c)
        limit = limit + 1

        global last_time, times_csv
        times_csv += str(limit) + ',' + str(time.time() - last_time) + '\n'
        last_time = time.time();
        
last_time = time.time()
sum_of_cubes(30)

f = open('images/test.csv','w+')
f.write(times_csv)
