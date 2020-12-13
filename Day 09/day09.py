from itertools import combinations

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [int(l.strip()) for l in lines]

    return lines

def Part1(lines):
    sol = None
    numbs = list(lines)

    for i in range(25,len(numbs)):
        valid = False
        for comb in combinations(numbs[i-25:i],2):
            if sum(comb) == numbs[i]:
                valid = True
                break
        if not valid:
            sol = numbs[i]
            break

    print("Part 1:")
    print("\t" + str(sol))
    print()
    return sol

def Part2(lines,invalid):
    numbs = list(lines)
    weakRange = None
    
    for size in range(2,len(numbs)):
        for i in range( len(numbs)-size+1 ):
            if sum(numbs[i:i+size]) == invalid:
                weakRange = numbs[i:i+size]
                break
        if weakRange:
            break

    sol = min(weakRange) + max(weakRange)

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
invalid = Part1(lines)
Part2(lines,invalid)