def readInput():
    out = [dict()]
    with open('input.txt') as fp:
        while( line := fp.readline() ):
            line = line.strip()
            if len(line) > 0:
                for sect in line.split(' '):
                    struct = sect.split(':')
                    out[-1][struct[0]] = struct[1]
            else:
                out.append(dict())

    return out

def Part1(lines):
    sol = 0

    for passport in lines:
        if all (k in passport for k in ('byr','iyr','eyr','hgt','hcl','ecl','pid')):
            sol += 1

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = 0

    for passport in lines:
        if all (k in passport for k in ('byr','iyr','eyr','hgt','hcl','ecl','pid')):
            try:
                if (
                        1920 <= int(passport['byr']) <= 2002 and
                        2010 <= int(passport['iyr']) <= 2020 and
                        2020 <= int(passport['eyr']) <= 2030 and
                        ( (passport['hgt'][-2:] == 'cm' and  150 <= int(passport['hgt'][:-2]) <= 193) or (passport['hgt'][-2:] == 'in' and  59 <= int(passport['hgt'][:-2]) <= 76) ) and
                        passport['hcl'][0] == '#' and len(passport['hcl']) == 7 and len([c for c in passport['hcl'][1:] if c not in '1234567890abcdef']) == 0 and
                        passport['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth'] and
                        int(passport['pid']) and len(passport['pid']) == 9
                ): sol += 1
            except:
                continue

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)