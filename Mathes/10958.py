import random

def eval_step(stack, operation):
    if operation == '+':
        stack.append(stack.pop() + stack.pop())
    elif operation == '*':
        stack.append(stack.pop() * stack.pop())
    elif operation == '-':
        stack.append(stack.pop() - stack.pop())
    elif operation == '/':
        stack.append(float(stack.pop()) / stack.pop())
    elif operation == '^':
        stack.append(stack.pop() ** stack.pop())

def eval(elements, expression):
    stack = []
    try:
        for op in expression:
            if type(op) is int:
                stack.append(elements[op])
            else:
                eval_step(stack, op)
        return stack
    except ZeroDivisionError:
        return [None]

def random_ex(element_count):
    expression = []
    queue = range(element_count)[::-1] # reversed for convenience
    stack_len = 0

    operators = [None, '+', '*', '-', '/'] # excluded exponentiation for speed

    while len(queue) > 0:
        if stack_len < 2:            
            expression.append(queue.pop())
            stack_len = stack_len + 1
        else:
            op = random.choice(operators)
            if op == None:
                expression.append(queue.pop())
                stack_len = stack_len + 1
            else:
                stack_len = stack_len - 1
                expression.append(op)

    for _ in range(stack_len - 1):
            op = random.choice(operators[1:])
            expression.append(op)
    return expression

def print_ex(elements, expression):
    result = ''
    for op in expression:
        if type(op) is int:
            result += str(elements[op])
        else:
            result += str(op)
        result += ' '
    print result

elements = range(1, 10)
expression = random_ex(9)
print_ex(elements, expression)
print eval(elements, expression)