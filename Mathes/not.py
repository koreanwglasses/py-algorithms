def compile(lines):
    nodes = []
    for line in lines:
        line = line.strip()

        if line == '':
            line = '"1":"0"'
        if line == ':':
            line = '"0":"1"'

        if ':' not in line:
            line = line + ':'
        f, t = line.split(':')
        
        felem = f.split('"')
        telem = t.split('"')

        if len(lines) <= 16:
            fconn =[int(conn, 16) for conn in list(''.join(''.join(felem[::2]).split(','))) if conn]
            tconn =[int(conn, 16) for conn in list(''.join(''.join(telem[::2]).split(','))) if conn]
        else:
            fconn = [int(conn, 16) for conn in ''.join(felem[::2]).split(',') if conn]
            tconn = [int(conn, 16) for conn in ''.join(telem[::2]).split(',') if conn]

        foutp = ''.join(felem[1::2])
        toutp = ''.join(telem[1::2])

        nodes.append((fconn, foutp, tconn, toutp))
    return nodes

def run(nodes, axioms):
    values = [False for _ in range(len(nodes))]
    values[:len(axioms)] = [bool(int(char)) for char in list(axioms)]
    
    output = ''

    for i in range(len(nodes)):
        fconn, foutp, tconn, toutp = nodes[i]
        if values[i]:
            output += toutp
            for j in tconn:
                values[j] = True
        else:
            output += foutp
            for j in fconn:
                values[j] = True
    
    print values
    print output

program =  '3:2' + '\n'
program += '3:2' + '\n'
program += '4' + '\n'
program += '4' + '\n'
program += ''

lines = program.split('\n')

nodes = compile(lines)
for axioms in ['00','01','10','11']:
    run(nodes,axioms)