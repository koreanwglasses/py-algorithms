from itertools import permutations

def check(solution, exclusions):
    for i in range(len(solution)):
        if i - 1 >= 0 and solution[i] in exclusions and solution[i - 1] in exclusions[solution[i]]:
            return False
        if i + 1 < len(solution) and solution[i] in exclusions and solution[i + 1] in exclusions[solution[i]]:
            return False
    return True

n = int(raw_input())
exclusions = {}
for _ in range(n):
    line = [int(num) for num in raw_input().split()]
    if line[1] != 0:
        exclusions[line[0]] = line[1:]

results = [solution for solution in permutations(range(1, n+1)) if check(solution, exclusions)]

if len(results) == 0:
    print 'There is no possible seating plan'
else:
    print 'We can seat people in order ' + ' '.join([str(p) for p in results[0]]) + ' ' + str(n + 1) 