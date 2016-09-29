from backtracking import Backtrack
import time

def pop_row(board, row):
    size = len(board)
    zeros = 0
    ones = 0
    for col in range(size):
        if board[row][col] == 0:
            zeros = zeros + 1
        if board[row][col] == 1:
            ones = ones + 1
    return [zeros, ones]

def pop_col(board, col):
    size = len(board)
    zeros = 0
    ones = 0
    for row in range(size):
        if board[row][col] == 0:
            zeros = zeros + 1
        if board[row][col] == 1:
            ones = ones + 1
    return [zeros, ones]

def get_candidates(board):
    
    size = len(board)
    
#    print_board(board)
#    time.sleep(.1)

    for row in range(size):
        for col in range(size):
            if board[row][col] == None:
                
                neighbors = []
                if row > 1 and board[row - 1][col] == board[row - 2][col]:
                    neighbors.append(board[row - 1][col])
                if col > 1 and board[row][col - 1] == board[row][col - 2]:
                    neighbors.append(board[row][col - 1])
                
                if row < size - 2 and board[row + 1][col] == board[row + 2][col]:
                    neighbors.append(board[row + 1][col])
                if col < size - 2 and board[row][col + 1] == board[row][col + 2]:
                    neighbors.append(board[row][col + 1])
                
                if row > 0 and row < size - 1 and board[row + 1][col] == board[row - 1][col]:
                    neighbors.append(board[row + 1][col])
                if col > 0 and col < size - 1 and board[row][col + 1] == board[row][col - 1]:
                    neighbors.append(board[row][col + 1])
                    
                row_pop = pop_row(board, row)
                col_pop = pop_col(board, col)
                    
                candidates = []
                
                if 1 not in neighbors and row_pop[1] < size / 2 and col_pop[1] < size / 2:
                    candidate = list(map(list, board))
                    candidate[row][col] = 1
                    candidates.append(candidate)
                    
                if 0 not in neighbors and row_pop[0] < size / 2 and col_pop[0] < size / 2:
                    candidate = list(map(list, board))
                    candidate[row][col] = 0
                    candidates.append(candidate)
                
                return candidates
                       
    return []
            
def to_char(s):
    if s == 1:
        return '1'
    if s == 0:
        return '0'
    if s == None:
        return '-'
    
def print_board(board):
    print('\n'.join(map(lambda row: ' '.join(map(to_char, row)), board)))
    print()
    
#def board_from_hints(hints, size):
#    board = [[None for col in range(size)] for row in range(size)]
#    for hint in hints:
#        r, c, v = hint
#        board[r][c] = v
#    return board

def parse_char(c):
    if c != '1' and c != '0':
        return None
    else:
        return int(c)

size, hints = map(int, input().split())

board = []
for _ in range(size):
    board.append(list(map(parse_char, input().split())))

print()
    
solver = Backtrack(get_candidates)
solution = solver.solve(board, size * size - hints)
print_board(solution)