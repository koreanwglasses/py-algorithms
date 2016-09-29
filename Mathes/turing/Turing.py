def get_list_index(head):
    if head < 0:
        return (False, -head - 1)
    else:
        return (True, head)

class UTM:
    def __init__(self, transitions):
        self.transitions = transitions
        self.head = 0
        self.state = None
        self.tapeleft = []
        self.taperight = []

    def move_left(self):
        self.head -= 1
        right, index = get_list_index(self.head)
        if not right and index >= len(self.tapeleft):
            self.tapeleft.append(None)

    def move_right(self):
        self.head += 1
        right, index = get_list_index(self.head)
        if right and index >= len(self.taperight):
            self.taperight.append(None)

    def read(self):        
        right, index = get_list_index(self.head)
        if right:
            return self.taperight[index]
        else:
            return self.tapeleft[index]

    def write(self, value):                
        right, index = get_list_index(self.head)
        if right:
            self.taperight[index] = value
        else:
            self.tapeleft[index] = value

    def step(self):

class Transitions:
    def __init__ (self):
        self.table = {}
    