from typing import List

class gameConsole:
    def __init__(self, comp: List[str]) -> None:
        self.accumulator = 0
        self.pos = 0
        self.prog = comp
        self.terminated = False

    def advance(self):
        if(not self.terminated):
            [op, val] = self.prog[self.pos].split(' ')
            val = int(val)

            if   op == 'acc':
                self.accumulator += val
            elif op == 'jmp':
                self.pos += val - 1 # Subtract 1 since we will increment 1
            elif op == 'nop':
                pass

            self.pos += 1

            if self.pos == len(self.prog):
                self.terminated = True