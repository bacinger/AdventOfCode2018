import re
from collections import defaultdict

inputs = []
content = open('input/day-16.txt').read().split('\n\n')
for val in content:
    inputs.append(val)
program = inputs[-1]
inputs.pop() # Remove program
inputs.pop() # Remove empty line

def addr(r, a, b):
    return r[a] + r[b]

def addi(r, a, b):
    return r[a] + b

def mulr(r, a, b):
    return r[a] * r[b]

def muli(r, a, b):
    return r[a] * b

def banr(r, a, b):
    return r[a] & r[b]

def bani(r, a, b):
    return r[a] & b

def borr(r, a, b):
    return r[a] | r[b]

def bori(r, a, b):
    return r[a] | b

def setr(r, a, b):
    return r[a]

def seti(r, a, b):
    return a

def gtir(r, a, b):
    if a > r[b]:
        return 1
    else:
        return 0

def gtri(r, a, b):
    if r[a] > b:
        return 1
    else:
        return 0

def gtrr(r, a, b):
    if r[a] > r[b]:
        return 1
    else:
        return 0

def eqir(r, a, b):
    if a == r[b]:
        return 1
    else:
        return 0

def eqri(r, a, b):
    if r[a] == b:
        return 1
    else:
        return 0

def eqrr(r, a, b):
    if r[a] == r[b]:
        return 1
    else:
        return 0

opcodes = {
    'addr': addr,
    'addi': addi,
    'mulr': mulr,
    'muli': muli,
    'banr': banr,
    'bani': bani,
    'borr': borr,
    'bori': bori,
    'setr': setr,
    'seti': seti,
    'gtir': gtir,
    'gtri': gtri,
    'gtrr': gtrr,
    'eqir': eqir,
    'eqri': eqri,
    'eqrr': eqrr,
}

def opcodes_keys():
    return set(opcodes.keys())

indeterminate = 0
possible = defaultdict(opcodes_keys)
for i in inputs:
    before, op, after = map(lambda s: list(map(int, re.findall(r'-?\d+', s))), i.splitlines())
    print(before, op, after)
    count = 0
    for opcode in opcodes:
        result = opcodes[opcode](before, op[1], op[2])
        if [*before[:op[3]], result, *before[op[3]+1:]] == after:
            count += 1
        elif opcode in possible[op[0]]:
            possible[op[0]].remove(opcode)
    if count >= 3:
        indeterminate += 1
print('Part 1:', indeterminate)

mapping = {}
while any(possible.values()):
    for n, o in possible.items():
        if len(o) == 1:
            mapping[n] = op = o.pop()
            for remaining in possible.values():
                remaining.discard(op)
regs = [0, 0, 0, 0]
for line in program.splitlines():
    op, a, b, c = [int(x) for x in line.split()]
    regs[c] = opcodes[mapping[op]](regs, a, b)
print('Part 2:', regs[0])