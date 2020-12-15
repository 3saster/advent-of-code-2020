# Rather than storing all entries of the game in a list, store a dict with the entries of the latest appearance of each number.
#
# The main benefit is that calculating the next number is a constant time operation; it does not depend on either
# how far in the game we are nor how many distinct numbers are in the game. Furthermore, the memory only depends on the number
# of distinct numbers in the game so far. In essence, if we know n numbers, calculating the (n+1)-th number this way takes O(1) time.
def elfGame(start,n):
    numbs = dict()
    for t in [(v,i+1) for i,v in enumerate(start[:-1])]:
        numbs[t[0]] = t[1]
    
    lastNum = start[-1]
    ind = len(start)

    addedNum = None
    while ind < n:
        try:
            addedNum = ind - numbs[lastNum]
        except KeyError:
            addedNum = 0
        numbs[lastNum]  = ind
        lastNum = addedNum
        ind += 1
    return addedNum

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return [ int(l) for l in lines[0].split(',') ]

def Part1(lines):
    sol = elfGame(lines,2020)

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = elfGame(lines,30000000)

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)