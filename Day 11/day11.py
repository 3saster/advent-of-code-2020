from copy import deepcopy

def inRange(arr,x,y):
    if 0 <= y < len(arr) and 0 <= x < len(arr[y]):
        return True
    return False

def neighbors(seats,x,y):
    neighbors = 0
    values = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

    for v in values:
        if inRange(seats,x+1*v[0],y+1*v[1]) and seats[y+1*v[1]][x+1*v[0]] == '#': neighbors += 1

    return neighbors

def visNeighbors(seats,x,y):
    neighbors = 0
    values = [(1,1),(1,0),(1,-1),(0,1),(0,-1),(-1,1),(-1,0),(-1,-1)]

    for v in values:
        i = 1
        while inRange(seats,x+i*v[0],y+i*v[1]):
            if   seats[y+i*v[1]][x+i*v[0]] == '#': neighbors += 1; break
            elif seats[y+i*v[1]][x+i*v[0]] == 'L': neighbors += 0; break
            i += 1

    return neighbors

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [list(l.strip()) for l in lines]

    return lines

def Part1(lines):
    seats = deepcopy(lines)
    seatsCopy = deepcopy(seats)

    start = False
    while seats != seatsCopy or start == False:
        start = True
        seats = deepcopy(seatsCopy)
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if   seats[y][x] == '.': seatsCopy[y][x] = '.'
                elif seats[y][x] == 'L' and neighbors(seats,x,y) == 0: seatsCopy[y][x] = '#'
                elif seats[y][x] == '#' and neighbors(seats,x,y) >= 4: seatsCopy[y][x] = 'L'

    sol = "".join(["".join(row) for row in seats]).count('#')

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    seats = deepcopy(lines)
    seatsCopy = deepcopy(seats)

    start = False
    while seats != seatsCopy or start == False:
        start = True
        seats = deepcopy(seatsCopy)
        for y in range(len(seats)):
            for x in range(len(seats[y])):
                if   seats[y][x] == '.': seatsCopy[y][x] = '.'
                elif seats[y][x] == 'L' and visNeighbors(seats,x,y) == 0: seatsCopy[y][x] = '#'
                elif seats[y][x] == '#' and visNeighbors(seats,x,y) >= 5: seatsCopy[y][x] = 'L'

    sol = "".join(["".join(row) for row in seats]).count('#')

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)