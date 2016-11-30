n = int(raw_input())
for _ in range(n):
    code = list(raw_input())
    raw_input()
    decode = [int(s) for s in raw_input().split()]
    msg = ''
    for i in decode:
        if i > 20:
            msg += ' '
        else:
            msg += code[i]
    print msg