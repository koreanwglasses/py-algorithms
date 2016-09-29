from backtracking import Backtrack
import time
import random

n = int(input())

def initial(n):
    queens = [[(0, col)] for col in range(n)]
    random.shuffle(queens)
    return queens

def get_candidates(queens):
    
#    print_board(queens)
#    time.sleep(.5)
    
    queen_cols = [c for r, c in queens]
    queen_diag_down = [r - c for r, c in queens]
    queen_diag_up = [r + c for r, c in queens]

    candidates = []
    
    row = queens[-1][0] + 1
    for col in range(n):
        if  (col not in queen_cols) and (row - col not in queen_diag_down) and (row + col not in queen_diag_up):
            candidate = list(queens)
            candidate.append((row, col))
            candidates.append(candidate)
    
    random.shuffle(candidates)
    return candidates
            
def print_board(queens):
    string = ''
    for row in range(n):
        for col in range(n):
            if (row, col) in queens:
#                string += str(queens.index((row, col))) + ' '
                string += '██'
            else:
                if (row + col) % 2 == 0:
                    string += '░░'
                else:
                    string += '  '
        string += '\n'
    
    print(string)
    
solver = Backtrack(get_candidates)
solution = solver.solve_mult(initial(n), n-1)
print_board(solution)