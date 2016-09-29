def BacktrackSolve(initial, getNext, check):
    solution = []
    tree = [initial]
    while True:
        while len(tree[-1]) == 0:
            tree.pop()
            solution.pop()

        next = tree[-1].pop(0)
        solution.append(next)

        tree.append(getNext(solution))
        
        if check(solution):
            return solution

def BacktrackSolve2(initial, getNext):
    tree = [initial]
    while True:
        while len(tree[-1]) == 0:
            tree.pop()

        solution = tree[-1].pop(0)
        
        next = getNext(solution)
        if next == True:
            return solution
        tree.append(next)



        