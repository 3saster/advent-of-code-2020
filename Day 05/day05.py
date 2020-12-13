def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return lines

def Part1(lines):
    seats = []
    for seat in lines:
        s = seat.replace('F','0').replace('L','0').replace('B','1').replace('R','1')
        seats.append( int(s,2) )
    sol = max(seats)

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    seats = []
    for seat in lines:
        s = seat.replace('F','0').replace('L','0').replace('B','1').replace('R','1')
        seats.append( int(s,2) )
    seats.sort()

    sol = 0
    for id in range(seats[0],seats[-1]+1):
        if id not in seats:
            sol = id
            break

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)