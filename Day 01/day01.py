from itertools import combinations
from math import prod

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    return [int(l.strip()) for l in lines]

def Part1(lines):
    sol = 0

    for v in combinations(lines,2):
        if sum(v) == 2020:
            sol = prod(v)
            break

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = 0

    for v in combinations(lines,3):
        if sum(v) == 2020:
            sol = prod(v)
            break

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)