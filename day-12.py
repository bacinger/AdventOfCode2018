fname = 'input/day-12.txt'
with open(fname) as f:
    initial_state = f.readline().split()[2]
    mappings = dict(line.strip().split(' => ') for line in f if line.strip())
          
def recenter(offset, state):
    pos = state.find('#')
    if pos >= 0:
        return offset + pos, state[pos:state.rfind('#') + 1]
    else:
        return 0, ''

def step(offset, state):
    extended = '....' + state + '....'
    new_pos = recenter(offset - 2, ''.join(mappings.get(extended[i:i + 5], '.') for i in range(len(state) + 4)))
    return new_pos

def grow(generations):
    seen = {}
    offset, state = recenter(0, initial_state)
    i = 0
    while i < generations:
        seen[state] = (i, offset)
        offset, state = step(offset, state)
        i += 1
        if state in seen:
            prev_i, prev_offset = seen[state]
            offset += (generations - i) // (i - prev_i) * (offset - prev_offset)
            i = generations - (generations - i) % (i - prev_i)
    return sum(offset + i for i, c in enumerate(state) if c == '#')

print('Part 1:', grow(20))
print('Part 2:', grow(50000000000))