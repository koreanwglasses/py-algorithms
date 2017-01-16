import backtracking2

def get_candidates_h(state):
    state, j = state
    c = []
    c.append([state[i] for i in [0,6,7,8,13,14,15,16,17]])
    c.append([state[i] for i in [1,2,3,4,5,10,11,12,21]])
    c.append([state[i] for i in [9,18,19,20,27,28,29,30,31]])
    c.append([state[i] for i in [22,23,24,25,26,33,34,35,44]])
    c.append([state[i] for i in [36,37,38,39,40,45,46,47,53]])
    c.append([state[i] for i in [32,41,42,43,48,49,50,51,52]])

    c.append([state[i] for i in range(1,9)])
    c.append([state[i] for i in range(9,18)])
    c.append([state[i] for i in range(18,27)])
    c.append([state[i] for i in range(27,36)])
    c.append([state[i] for i in range(36,45)])
    c.append([state[i] for i in range(45,53)])

    c.append([state[i] for i in [2,3,9,10,18,19,27,28]])
    c.append([state[i] for i in [4,5,11,12,20,21,29,30,36]])
    c.append([state[i] for i in [0,6,7,13,14,31,37,38,45]])
    c.append([state[i] for i in [8,15,16,22,39,40,46,47,53]])
    c.append([state[i] for i in [17,23,24,32,33,41,42,48,49]])
    c.append([state[i] for i in [25,26,34,35,43,44,50,51]])

    c.append([state[i] for i in [7,8,16,17,24,25,35]])
    c.append([state[i] for i in [5,6,14,15,22,23,33,34,44]])
    c.append([state[i] for i in [3,4,12,13,32,42,43,51,52]])
    c.append([state[i] for i in [1,2,10,11,21,40,41,49,50]])
    c.append([state[i] for i in [9,19,20,30,31,38,39,47,48]])
    c.append([state[i] for i in [18,28,29,36,37,45,46,53]])

    for cl in c:
        ncl = [x for x in cl if x != -1]
        if len(ncl) != len(set(ncl)):
            return [] 
    
    if -1 not in state:
        return True

    if state[j] != -1:
        return [(list(state), j+1)]

    newstates = []
    for n in range(1, 10):
        newstate = list(state)
        newstate[j] = n
        newstates.append((newstate, j + 1))
    return newstates

def get_candidates(state):
    state, k = state

    c = []
    for j in [0,27,90,153,180]:
        c.append([state[i + j] for i in [0,1,2,9,10,11,18,19,20]])
        c.append([state[i + 3 + j] for i in [0,1,2,9,10,11,18,19,20]])
        c.append([state[i + 6 + j] for i in [0,1,2,9,10,11,18,19,20]])
    for j in [54,117]:
        c.append([state[i + j] for i in [0,1,2,12,13,14,24,25,26]])
        c.append([state[i + 3 + j] for i in [0,1,2,12,13,14,24,25,26]])
        c.append([state[i + 6 + j] for i in [0,1,2,12,13,14,24,25,26]])
        c.append([state[i + 9 + j] for i in [0,1,2,12,13,14,24,25,26]])
    for j in [0,9,18,27,36,45,54,57,66,69,78,81,90,99,108,117,129,132,141,144,153,162,171,180,189,198]:        
        c.append([state[i + j] for i in range(9)])
    for j in range(9):
        c.append([state[i + j] for i in [0,9,18,27,36,45,54,66,78]])
        c.append([state[i + j] for i in [57,69,81,90,99,108,117,129,141]])
        c.append([state[i + j] for i in [120,132,144,153,162,171,180,189,198]])
    
    for cl in c:
        ncl = [x for x in cl if x != -1]
        if len(ncl) != len(set(ncl)):
            return [] 
    
    if -1 not in state:
        return True

    if state[k] != -1:
        return [(list(state), k+1)]

    newstates = []
    for n in range(1, 10):
        newstate = list(state)
        newstate[k] = n
        newstates.append((newstate, k+1))
    return newstates

print backtracking2.BacktrackSolve2([(
    [
        2,-1,-1, -1,9,-1, -1,3,4,
        -1,-1,5, 4,7,-1, -1,-1,9,
        -1,9,8, -1,3,-1, 1,-1,-1,

        -1,1,-1, 5,-1,7, -1,9,-1,
        7,5,2, -1,8,-1, 6,4,1,
        -1,-1,-1, 1,-1,6, -1,-1,-1,

        -1,-1,1, -1,6,-1, -1,2,-1, -1,8,1,
        5,2,-1, 9,1,-1, -1,8,-1, -1,-1,5,
        9,6,-1, 2,5,-1, -1,1,-1, 6,-1,-1,
        
            -1,-1,-1, 8,-1,9, -1,-1,-1,
            3,8,9, -1,6,-1, 1,5,4,
            -1,-1,-1, 3,-1,1, -1,-1,-1,

            -1,-1,2, -1,7,-1, -1,9,-1, -1,3,5,
            6,-1,-1, -1,3,-1, -1,4,2, -1,-1,9,
            8,4,-1, -1,9,-1, -1,1,-1, 7,-1,-1,

                -1,-1,-1, 2,-1,1, -1,-1,-1,
                9,1,5, -1,8,-1, 4,2,3,
                -1,6,-1, 4,-1,9, -1,5,-1,

                -1,-1,9, -1,7,-1, 6,1,-1,
                3,-1,-1, -1,6,4, 5,-1,-1,
                7,8,-1, -1,2,-1, -1,-1,4

    ],0)], get_candidates)
