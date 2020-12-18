from collections import defaultdict
from itertools import product
import operator

def addTuple(t1,t2):
    return type(t1)(map(operator.add, t1, t2))

def cubeSol(lines,n,dim):
    # Make Cube Dict
    keys = [(y,x)+(0,)*(dim-2) for y,l in enumerate(lines) for x,_ in enumerate(l) if lines[x][y]=='#']

    # Init Active Cubes
    cubes = defaultdict(lambda: [False,0,False,0])
    for k in keys:
        cubes[k] = [True,0,True,0]
    # Init Neighbors
    loopKeys = list(cubes.keys())
    neighborRanges = set(product( (-1,0,1), repeat=dim ))
    neighborRanges.remove( (0,)*dim )

    for c in loopKeys:
        if cubes[c][0]:
            for tup in neighborRanges:
                cubes[ addTuple(c,tup) ][1] += 1
                cubes[ addTuple(c,tup) ][3] += 1
    # Advance stages
    for _ in range(n):
        advanceStage(cubes,dim)

    return len([c for c in cubes.keys() if cubes[c][0]])

def advanceStage(cubes,dim):
    loopKeys = list(cubes.keys())
    neighborRanges = set(product( (-1,0,1), repeat=dim ))
    neighborRanges.remove( (0,)*dim )

    for c in loopKeys:
        # Active cube being deactivated
        if cubes[c][0] == True and ( cubes[c][1] != 2 and cubes[c][1] != 3 ):
            cubes[c][2] = False
            for tup in neighborRanges:
                # neighbors of adjacent cubes go down 1 in next stage
                cubes[ addTuple(c,tup) ][3] -= 1
        # Inactive cube being activated
        elif cubes[c][0] == False and ( cubes[c][1] == 3 ):
            cubes[c][2] = True
            for tup in neighborRanges:
                # neighbors of adjacent cubes go up 1 in next stage
                cubes[ addTuple(c,tup) ][3] += 1

    # Update neighbors in next stage
    loopKeys = list(cubes.keys())
    for c in loopKeys:
        if cubes[c][3]==0 and cubes[c][2]==False: 
            del cubes[c]
        else:
            cubes[c][0:2] = cubes[c][2:4]

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return lines

def Part1(lines):
    sol = cubeSol(lines,6,3)

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = cubeSol(lines,6,4)

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)