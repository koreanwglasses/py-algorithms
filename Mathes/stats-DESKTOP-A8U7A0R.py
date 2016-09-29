import random

n = 100000

def test():
    s = random.sample(range(52),4)
    s = list(map(lambda c: c % 13, s))
    
    if len(s) > len(set(s)):
        return True

count = 0
for _ in range(n):
    if test():
        count = count + 1
print(count / n)