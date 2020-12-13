from console import gameConsole

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return lines

def Part1(lines):
    console = gameConsole(lines)

    passed = []

    while (p:=console.pos) not in passed:
        passed.append(p)
        console.advance()

    sol = console.accumulator

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = None

    for i in range(len(lines)):
        prog = list(lines)
        if prog[i][0:3] == 'nop':
            prog[i] = prog[i].replace('nop','jmp')
        elif prog[i][0:3] == 'jmp':
            prog[i] = prog[i].replace('jmp','nop')
        elif prog[i][0:3] == 'acc':
            continue

        console = gameConsole(prog)

        passed = []
        while not console.terminated and (p:=console.pos) not in passed :
            passed.append(p)
            console.advance()

        if console.terminated:
            sol = console.accumulator
            break

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)