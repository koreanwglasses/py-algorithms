import mathes3
import stats
#n = eval(raw_input())
#print mathes.prime_factors(n)
#count = 0
#while True:
#    print(count)
#    print(mathes.prime_factors(n))
#    n = sum(mathes.factors(n)) - n
#    print(n)
#    count += 1
#    raw_input()

#p_memo = [1,1,2,3,5]
#def p(n,m):
#    if n < 0:
#        return 0
#    if n < len(p_memo):
#        return p_memo[n]
#    
#    if m > n:
#        m = n
#    
#    s = 0
#    for k in range(1, m):
#        s += p(n - k, k)
#        
#    return s
#
#def partitions(n):
#    return p(n,n)
#        
#while True:
#    print(partitions(eval(raw_input())))

#print([mathes3.telephone(n) for n in range(100)])

print(stats.random())