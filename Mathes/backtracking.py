class Backtrack:
    def __init__(self, get_candidates):
        self.get_candidates = get_candidates
        
    def solve_recursive(self, initial, depth):
        if depth == 0:
            return initial
        else:
            candidates = self.get_candidates(initial)
            
            for candidate in candidates:
                solution = self.solve(candidate, depth - 1)
                if solution != None:
                    return solution
            return None
        
    def solve_mult(self, initial, max_depth, eliminated=None): # Returns the solution if it exists
        tree = [initial] # Initialize tree with initial conditions.
        
        depth = 0 # Set initial traversal depth to 0

        while True:            
            if len(tree[depth]) == 0: # If the current branch is empty (i.e. parent node produced no children, thus indicating a dead end)...                 
                # Callback
                if eliminated is not None: 
                    eliminated(tree[depth][0])
                
                del tree[depth]    # Remove empty branch                
                depth = depth - 1  # Go up a branch
                del tree[depth][0] # Remove parent node
            else:                
                this = tree[depth][0] # Get the next candidate for an incomplete the solution

                # If you have reached the max depth (i.e. solution is complete), return the solution
                if depth == max_depth:
                    return this                
                
                children = self.get_candidates(this) # Otherwise, generate more candidates to continue the solution.
                                                     # If the function detects that the incomplete solution cannot lead to a complete solution, 
                                                     # the children should be an empty list.
                
                # Increase the depth counter and append the children to the tree before looping
                depth = depth + 1
                tree.append(children)
                
    def solve(self, initial, max_depth, eliminated=None):
        tree = [[initial]]
        
        depth = 0
        while True:            
            if len(tree[depth]) == 0:
                del tree[depth]
                
                depth = depth - 1
                
                if eliminated is not None:
                    eliminated(tree[depth][0])
                    
                del tree[depth][0]
            else:
                this = tree[depth][0]

                if depth == max_depth:
                    return this
                
                children = self.get_candidates(this)
                
                depth = depth + 1
                tree.append(children)