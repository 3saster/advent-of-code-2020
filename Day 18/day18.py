def evalExp(input,part):
    # If the input is a number (figuratively or literally), return that number
    if type(input) is int or input in '1234567890':
        return int(input)

    nodes = ['']
    ops = []

    # Otherwise, split the into the top level arguments (nodes) and operations (op)
    i = 0
    while i < len(input):
        if input[i] in '1234567890': nodes[-1] += input[i]
        elif input[i] in '+*':
            ops.append(input[i])
            nodes.append('')
        elif input[i] == '(':
            i += 1
            depth = 1
            while depth > 0:
                if   input[i] == '(' : depth += 1
                elif input[i] == ')' : depth -= 1
                nodes[-1] += input[i]
                i += 1
            nodes[-1] = nodes[-1][:-1]
            i -= 1
        i += 1

    # Now evaluate each top level node recursively, then all the nodes will be plain numbers
    # Then perform the rules depending on the part
    if part==1: # Part 1
        while len(nodes) >= 2:
            if ops[0] == '+':
                nodes[1] = evalExp(nodes[0],1) + evalExp(nodes[1],1)
            elif ops[0] == '*':
                nodes[1] = evalExp(nodes[0],1) * evalExp(nodes[1],1)
            del nodes[0]
            del ops[0]
        return int(nodes[0])
    elif part==2: # Part 2
        while len(nodes) >= 2:
            if '+' in ops:
                ind = ops.index('+')
                nodes[ind+1] = evalExp(nodes[ind],2) + evalExp(nodes[ind+1],2)
                del nodes[ind]
                del ops[ind]
            else:
                nodes[1]     = evalExp(nodes[0],2) * evalExp(nodes[1],2)
                del nodes[0]
                del ops[0]
        return int(nodes[0])

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip().replace(' ','') for l in lines]

    return lines

def Part1(lines):
    sol = sum( [evalExp(exp,1) for exp in lines] )

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = sum( [evalExp(exp,2) for exp in lines] )

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)