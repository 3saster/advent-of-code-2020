from math import ceil
from functools import reduce

def euclideanAlgorithm(a,b):
    (old_r, r) = (a, b)
    (old_s, s) = (1, 0)
    (old_t, t) = (0, 1)
    
    while r != 0:
        quotient = old_r//r
        (old_r, r) = (r, old_r - quotient * r)
        (old_s, s) = (s, old_s - quotient * s)
        (old_t, t) = (t, old_t - quotient * t)
    
    # Bezout coefficients; gcd
    return (old_s, old_t, old_r)

# Solution to x = t1[0] mod t1[1], x = t2[0] mod t2[1]
def pairwiseCong(t1,t2):
    (a,m) = t1
    (b,n) = t2
    (u,v,g) = euclideanAlgorithm( t1[1], t2[1] )
    return ( (a*v*n + b*u*m)//g % (m*n//g), (m*n//g) )

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return lines

def Part1(lines):
    depart = int(lines[0])
    buses = [int(ID) for ID in lines[1].split(',') if ID != 'x']

    departTimes = [ID*ceil(depart/ID) for ID in buses]
    busIndex = departTimes.index(min(departTimes))

    sol = buses[busIndex] * ( departTimes[busIndex] - depart )

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    buses = [ (int(ID),i) for ID,i in zip( lines[1].split(','), range(len(lines[1])) ) if ID != 'x']
    equations = [(-b%a,a) for a,b in buses]
    # This becomes a system of congruences; we can find the solution by the Chinese Remainder Theorem
    busTimes = reduce(pairwiseCong, equations )

    sol = busTimes[0]

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)