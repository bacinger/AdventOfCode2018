from collections import defaultdict
from string import ascii_lowercase

parsed = set()
toparse = defaultdict(set)
count = defaultdict(set)
part1 = ''
fname = 'input/day-07.txt'
with open(fname) as f:
    content = f.read().splitlines()
    for val in content:
        w = val.split()
        a = w[1]
        b = w[7]
        toparse[b].add(a)
        count[a].add(b)

for _ in range(len(count)+1):
    for letter in ascii_lowercase:
        ul = letter.upper()
        if ul not in parsed:
            if toparse[ul] & parsed == toparse[ul]:
                part1 += ul
                parsed.add(ul)
                break

print('Part 1:', part1)

alphabet = []
for letter in ascii_lowercase:
    alphabet.append(letter.upper())
parsed = set()
workingon = [None] * 5
timeleft = [0] * 5
for i in range(1000):
    for j in range(5):
        if workingon[j] is not None:
            timeleft[j] -= 1
            if timeleft[j] == 0:
                parsed.add(workingon[j])
                workingon[j] = None
    if set(alphabet) == parsed:
        print('Part 2:', i)
        break
    for j in range(5):
        if workingon[j] is not None:
            continue
        for k in alphabet:
            if k not in parsed and k not in workingon:
                if toparse[k] & parsed == toparse[k]:
                    workingon[j] = k
                    timeleft[j] = 60 + ord(k) - ord('A') + 1
                    break