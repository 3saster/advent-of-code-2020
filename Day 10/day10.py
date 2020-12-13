from functools import lru_cache
from math import prod

# Offset Tribonacci numbers
# The (n+2)-th Tribonacci number is the number of ways a set with n elements can be partitioned subsets of size 1, 2, or 3
# I found this by determining the generating function
# [sum of (x+x^2+x^3)^n from n=0 to infinity] = 1/(1-x-x^2-x^3)
@lru_cache(maxsize=None)
def trib_off(n):
    if n==0: return 1
    elif n<3: return n

    return trib_off(n-1) + trib_off(n-2) + trib_off(n-3)

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [int(l.strip()) for l in lines]

    return lines

def Part1(lines):
    jolts = list(lines)
    jolts.append(0)
    jolts.sort()
    jolts.append(jolts[-1]+3)

    joltDiff = [ b-a for a,b in zip(jolts[:-1],jolts[1:]) ]

    sol = joltDiff.count(1) * joltDiff.count(3)

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    jolts = list(lines)
    jolts.append(0)
    jolts.sort()
    jolts.append(jolts[-1]+3)

    joltDiff = [ b-a for a,b in zip(jolts[:-1],jolts[1:]) ]

    # This counts consecutive 1's in JoltDiff
    contRange = [len(r) for r in ''.join([str(v) for v in joltDiff]).split('3') if len(r)>=2]

    # Essentially, we can replace a (1,1) with a (2); this amounts to a middle charger
    # Likewise, we can replace a (1,1,1) with a (3); this amounts to removing 2 middle chargers
    # Each range of n contiguous 1's has trib_off(n) ways to remove chargers in this way
    # that is; partition a set of n 1's into subsets of size 1, 2, or 3
    sol = prod([trib_off(c) for c in contRange])

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)