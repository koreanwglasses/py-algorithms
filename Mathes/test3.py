a = raw_input()
b = raw_input()

prev = [0 for _ in range(len(a))]
for i in range(len(a)):
    last = 0
    corner = 0
    for j in range(len(b)):
        if a[i] == b[j]:
            val = 1 + corner
        else:
            val = max(last, prev[j])
        last = val
        corner = prev[j]
        prev[j] = val

print prev[-1]

# Enter your code here. Read input from STDIN. Print output to STDOUT