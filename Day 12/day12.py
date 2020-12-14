import operator
from math import cos,sin,pi
def addTuple(t1,t2):
    return type(t1)(map(operator.add, t1, t2))
def subTuple(t1,t2):
    return type(t1)(map(operator.sub, t1, t2))
def scaleTuple(tup,n):
    return type(tup)([n*d for d in tup])
def rotTuple(tup,angle):
    (x,y) = tup
    t = pi/180 * angle
    return ( x*cos(t)-y*sin(t), x*sin(t)+y*cos(t))

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return lines

def Part1(lines):
    pos = (0,0)
    shipDir = 'E'

    comp = ['N','E','S','W']
    compdir = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}

    for dir in lines:
        instr = dir[0]
        value = int(dir[1:])

        if instr in comp:
            pos = addTuple( scaleTuple(compdir[instr],value) , pos)
        elif instr == 'R':
            shipDir = comp[ (comp.index(shipDir) + value//90)%4 ]
        elif instr == 'L':
            shipDir = comp[ (comp.index(shipDir) - value//90)%4 ]
        elif instr == 'F':
            pos = addTuple( scaleTuple(compdir[shipDir],value) , pos)

    sol = sum( [abs(x) for x in pos] )

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    shipPos = (0,0)
    waypPos = (10,1)

    comp = ['N','E','S','W']
    compdir = {'N':(0,1),'E':(1,0),'S':(0,-1),'W':(-1,0)}

    for dir in lines:
        instr = dir[0]
        value = int(dir[1:])

        if instr in comp:
            waypPos = addTuple( scaleTuple(compdir[instr],value) , waypPos)
        elif instr == 'R':
            waypPos = addTuple( rotTuple( subTuple(waypPos,shipPos), -value), shipPos )
        elif instr == 'L':
            waypPos = addTuple( rotTuple( subTuple(waypPos,shipPos), +value), shipPos )
        elif instr == 'F':
            waypDist = subTuple(waypPos,shipPos)
            shipPos = addTuple(shipPos,scaleTuple(waypDist,value))
            waypPos = addTuple(waypPos,scaleTuple(waypDist,value))

    sol = round( sum( [abs(x) for x in shipPos] ) )

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)