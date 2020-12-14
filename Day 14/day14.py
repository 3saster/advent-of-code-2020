def flatten(list):
    return [item for v in list for item in v]

def applyBitmask(mask, num):
    return "".join([ (m+n).strip()[0] for m,n in zip(mask,num)])
def applyMemmask(mask, address):
    return "".join([ (m+n).strip()[0] for m,n in zip(mask,address)])

def memoryAddressEncode(address):
    if 'X' not in address:
        return [address]
    (add1,add2) =( address.replace('X','0',1), address.replace('X','1',1) )
    return flatten([memoryAddressEncode(add1),memoryAddressEncode(add2)])

def readInput():
    with open('input.txt') as fp:
        lines = fp.readlines()
    lines = [l.strip() for l in lines]

    return [s.split(',') for s in ",".join(lines).split("mask = ") if len(s)>0]

def Part1(lines):
    memory = dict()
    for maskLayer in lines:
        mask = maskLayer[0].replace('X',' ')
        for instr in maskLayer[1:]:
            if len(instr)==0: continue
            # convert number to binary
            num = int(instr.split(" = ")[1])
            num = "{0:036b}".format(num)
            # apply mask to number
            newNum = int(applyBitmask(mask,num),2)
            address = int(instr[ instr.index('[')+1:instr.index(']') ])
            # set memory
            memory[address] = newNum

    sol = sum(memory.values())

    print("Part 1:")
    print("\t" + str(sol))
    print()

def Part2(lines):
    memory = dict()
    for maskLayer in lines:
        mask = maskLayer[0].replace('0',' ')
        for instr in maskLayer[1:]:
            if len(instr)==0: continue
            # convert address to binary
            address = int(instr[ instr.index('[')+1:instr.index(']') ])
            address = "{0:036b}".format(address)
            
            num = int(instr.split(" = ")[1])

            # set memory for each possible address
            for add in memoryAddressEncode( applyMemmask(mask,address) ):
                memory[ int(add,2) ] = num 

    sol = sum(memory.values())

    print("Part 2:")
    print("\t" + str(sol))
    print()

# Execution stuff
lines = readInput()
Part1(lines)
Part2(lines)