def readInput():
    out = []

    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]
    for l in lines:
        pair = l.split(': ')
        pair[0] = pair[0].split(' ')
        pair[0][0] = tuple([int(n) for n in pair[0][0].split('-')])

        out.append( [ pair[0][0], pair[0][1], pair[1] ] )

    return out

def Part1(lines):
    sol = 0

    for password in lines:
        counted = password[2].count( password[1] )
        if password[0][0] <= counted <= password[0][1]:
            sol += 1

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = 0

    for password in lines:
        passcode = password[2]
        first  = passcode[ password[0][0]-1 ]
        second = passcode[ password[0][1]-1 ]

        if (first == password[1] or second == password[1]) and first != second:
            sol += 1

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)