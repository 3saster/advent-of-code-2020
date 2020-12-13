def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return lines

def Part1(lines):
    sol = 0

    group = ''
    for question in lines:
        if question != '':
            group += question
        else:
            sol += len(set(group))
            group = ''
    # in case last group is left
    if group != '':
        sol += len(set(group))

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    sol = 0

    group = []
    for question in lines:
        if question != '':
            group.append(question)
        else:
            answers = set(''.join(group))
            for g in group:
                answers = [ans for ans in answers if ans in g]
            sol += len(answers)
            group = []
    # in case last group is left
    if group != '':
        answers = set(''.join(group))
        for g in group:
            answers = [ans for ans in answers if ans in g]
        sol += len(answers)

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)