class Turing2D:
    def __init__(self):
        self.tape = Tape2D()
        self.head = (0,0)

    def __str__(self):
        tape = self.tape.to_array()
        string = ''
        for row in tape:
            line = ''
            for value in row:
                if value:
                    line += '#'
                else:
                    line += ' '
            string += line
            string += '\n'
        return string

class Tape2D:
    def __init__(self, initial_width=16, initial_height=16, expansion_step=8, default_value=False):
        self.default_value = default_value
        self.expansion_step = expansion_step

        self.q1 = [[default_value]]
        self.q2 = [[default_value]]
        self.q3 = [[default_value]]
        self.q4 = [[default_value]]

        self.right = 0
        self.left = -1
        self.top = 0
        self.bottom = -1

        self.expand_up(initial_height // 2 - 1) 
        self.expand_down(initial_height // 2 - 1)
        self.expand_left(initial_width // 2 - 1)
        self.expand_right(initial_width // 2 - 1)

    def __repr__(self):
        return '<q1: {}x{}, q2: {}x{}, q3: {}x{}, q4: {}x{}>'.format(len(self.q1), len(self.q1[0]), len(self.q2), len(self.q2[0]), len(self.q3), len(self.q3[0]), len(self.q4), len(self.q4[0]))

    def to_array(self):
        return [self.q2[r] + self.q1[r] for r in range(self.top, -1, -1)] + [self.q3[r] + self.q4[r] for r in range(-self.bottom)]

    def index(self, x, y):
        if x > self.right:
            self.expand_right(self.expansion_step)
        elif x < self.left:
            self.expand_left(self.expansion_step)
        
        if y > self.top:
            self.expand_up(self.expansion_step)
        elif y < self.bottom:
            self.expand_down(self.expansion_step)

        if x >= 0:
            if y >= 0:
                return (self.q1, x, y)
            else:
                return (self.q4, x, -y - 1)
        else:
            if y >= 0:
                return (self.q2, -x - 1, y)
            else:
                return (self.q3, -x - 1, -y - 1)

    def read(self, x, y):
        q, x, y = self.index(x, y)
        return q[x][y]

    def write(self, x, y, value):        
        q, x, y = self.index(x, y)
        q[x][y] = value

    def expand_up(self, amount):
        self.q1.extend([[self.default_value for i in range(len(self.q1[0]))] for j in range(amount)])
        self.q2.extend([[self.default_value for i in range(len(self.q2[0]))] for j in range(amount)])
        self.top += amount

    def expand_right(self, amount):
        for row in self.q1:
            row.extend([self.default_value for i in range(amount)])
        for row in self.q4:
            row.extend([self.default_value for i in range(amount)])
        self.right += amount

    def expand_down(self, amount):
        self.q3.extend([[self.default_value for i in range(len(self.q3[0]))] for j in range(amount)])
        self.q4.extend([[self.default_value for i in range(len(self.q4[0]))] for j in range(amount)])
        self.bottom -= amount

    def expand_left(self, amount):
        for row in self.q2:
            row.extend([self.default_value for i in range(amount)])
        for row in self.q3:
            row.extend([self.default_value for i in range(amount)])
        self.left -= amount

if __name__ == '__main__':
    turing = Turing2D()

    for i in range(10):
        turing.tape.write(i, i, True)

    print(turing)