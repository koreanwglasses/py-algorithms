def gen(a, b, c, rule):
    condition = (a << 2) + (b << 1) + c
    if ((1 << condition) & rule) == 0:
        return 0
    else:
        return 1
        

def iterate(board, rule):
    next_gen = [0] * len(board)
    next_gen[0] = gen(0, board[0], board[1], rule)
    for i in range(1, len(board) - 1):
        next_gen[i] = gen(board[i - 1], board[i], board[i + 1], rule)
    next_gen[-1] = gen(board[-2], board[-1], 0, rule)
    
    return next_gen

width = int(input()) #115
while True:
    rule, height = map(int, input().split())
    init = [0] * width
    init[width // 2] = 1
    
    for _ in range(height):
        print("".join(map(str,init)).replace("0", "  ").replace("1", "██"))
        init = iterate(init, rule)