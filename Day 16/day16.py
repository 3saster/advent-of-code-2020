from math import prod

def flatten(list):
    return [item for v in list for item in v]

# convert 'a-b or c-d or ...' to a set of valid numbers
def rangeValues(ranges):
    out = set()
    for r in ranges.split(' or '):
        parts = r.split('-')
        for p in range(int(parts[0]),int(parts[1])+1):
            out.add(p)
    return out


def readInput():
    with open('input.txt') as fp:
        lines = fp.read()
    lines = [l.split('\n') for l in lines.split('\n\n')]

    return lines

def Part1(lines):
    validFields = [True for _ in range( len(lines[2][1:]) )]
    tickets = [ l for l in lines[2][1:] if len(l)>0 ]
    ranges = [ l.split(': ')[1] for l in lines[0] ]

    validSet = set(flatten([rangeValues(r) for r in ranges]))

    sol = 0
    for i in range( len(tickets) ):
        for f in [int(t) for t in tickets[i].split(',')]:
            if f not in validSet:
                sol += f
                validFields[i] = False

    print("Part 1:")
    print("\t" + str(sol))
    print()
    return validFields

def Part2(lines,validFields):
    fields = [ l.split(': ')[0] for l in lines[0] ]
    ranges = [ l.split(': ')[1] for l in lines[0] ]
    validSet = [rangeValues(r) for r in ranges]

    # valid tickets
    tickets = [t for i,t in enumerate(lines[2][1:]) if validFields[i]==True]
    tickets = [t.split(',') for t in tickets if len(t)>0]

    # figure out what each field COULD be
    candidates = [ set() for _ in range( len(tickets[0]) ) ]
    for i in range( len(tickets[0]) ):
        field_i = [int(t[i]) for t in tickets]
        for ind,validRanges in enumerate(validSet):
            # if all entries are valid
            if len( [inv for inv in field_i if inv not in validRanges] ) == 0:
                candidates[i].add( fields[ind] )

    # process of elimination
    ticketFields = [ None for _ in range( len(tickets[0]) ) ]
    while None in ticketFields:
        loneField = [(ind,list(c)[0]) for ind,c in enumerate(candidates) if len(c)==1][0]
        ticketFields[ loneField[0] ] = loneField[1]
        for c in candidates:
            if loneField[1] in c: c.remove( loneField[1] )

    santaTicket = [int(l) for l in lines[1][1].split(',')]
    sol = prod( [santaTicket[i] for i,f in enumerate(ticketFields) if 'departure' in f] )

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
validFields = Part1(lines)
Part2(lines,validFields)