from math import prod

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return lines

def slopeCheck(trees, xvel, yvel):
    sol = 0

    x = 0
    y = 0
    while y < len(trees):
        if trees[y][x] == '#':
            sol += 1
        y += yvel
        x = (x+xvel) % len(trees[0])
    return sol

def Part1(lines):
    sol = slopeCheck(lines,3,1)

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = prod( [ slopeCheck(lines,1,1), slopeCheck(lines,3,1), slopeCheck(lines,5,1), slopeCheck(lines,7,1), slopeCheck(lines,1,2) ] )

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)