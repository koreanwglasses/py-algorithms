import turtle
def iterate(start, rules, iterations):
    for _ in range(iterations):
        start = start.translate(rules)
    return start

stack = []
def push_turtle():
    stack.append((turtle.pos(), turtle.heading()))
    
def pop_turtle():
    pos, heading = stack.pop()
    
    turtle.penup()
    turtle.setpos(pos)
    turtle.setheading(heading)
    turtle.pendown()

std_actions = {'F': (lambda: turtle.forward(1.5)),
              '+': (lambda: turtle.right(60)),
              '-': (lambda: turtle.left(60)),
              '[': push_turtle,
              ']': pop_turtle}
  
def turtle_draw(string, actions=std_actions):
    for char in list(string):
        if char in actions:
            actions[char]()            

if __name__ == '__main__':
    actions = std_actions.copy()
#    rules = {ord('X'): 'X+YF+', ord('Y'): '-FX-Y'}
#    initial = 'FX'
    
#    rules = {ord('1'): '11', ord('0'): '1[-0]+0'}
#    initial = '0'
#    actions.update({'0': std_actions['F'], '1': std_actions['F']})

    turtle.penup()
    turtle.setpos(-400, 300)
    turtle.pendown()
    
    rules = {ord('A'): '+B-A-B+', ord('B'): '-A+B+A-'}
    initial = 'A'
    actions.update({'A': std_actions['F'], 'B': std_actions['F']})
    
    string = iterate(initial, rules, 9)
    
    print(string)
    
    turtle.speed(0)
    turtle.hideturtle()
    turtle_draw(string, actions)
    turtle.done()