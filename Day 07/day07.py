def flatten(list):
    return [item for v in list for item in v]

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    out = dict()
    for l in lines:
        key = l.split(' contain ')[0][:-5]
        bags = [s.strip().replace('.','') for s in l.split(' contain ')[1].split(',')]
        try:
            value = [ int(b.split(' ')[0]) * [' '.join(b.split(' ')[1:-1])] for b in bags]
            value = flatten(value)
        except ValueError: # no other bags
            value = []
        out[key] = value
    return out

def Part1(lines):
    sol = 0
    
    bagDict = dict(lines)
    for bag in bagDict.keys():
        outerBags = [bag]
        innerBags = list(set(bagDict[bag]))
        while outerBags != innerBags:
            if 'shiny gold' in innerBags:
                sol += 1
                break
            outerBags = list(innerBags)
            innerBags = list(set(flatten([bagDict[s] for s in innerBags])))

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = 0
    
    bagDict = dict(lines)
    outerBags = ['shiny gold']
    innerBags = bagDict['shiny gold']
    while outerBags != innerBags:
        sol += len(innerBags)
        outerBags = list(innerBags)
        innerBags = flatten([bagDict[s] for s in innerBags])

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)