from collections import defaultdict

def distance(x1,y1,x2,y2):
     return abs(x1-x2) + abs(y1-y2)

Cs = []
fname = 'input/day-06.txt'
with open(fname) as f:
    content = f.read().splitlines()
    for val in content:
        x, y = [int(c) for c in val.split(',')]
        Cs.append((x,y))

xmin = min([x for x,y in Cs])
xmax = max([x for x,y in Cs])
ymin = min([y for x,y in Cs])
ymax = max([y for x,y in Cs])

map1 = defaultdict(int)
for i in range(xmin, xmax):
    for j in range (ymin, ymax):
        ds = [(distance(c[0], c[1], i, j), c) for c in Cs]
        ds.sort()
        if ds[0][0] < ds[1][0]:
            map1[ds[0][1]] += 1

map2 = defaultdict(int)
for i in range(xmin-400, xmax+400):
    for j in range (ymin-400, ymax+400):
        ds = [(distance(c[0], c[1], i, j), c) for c in Cs]
        ds.sort()
        if ds[0][0] < ds[1][0]:
            map2[ds[0][1]] += 1

# Catching points that extend infinitely
part1 = [(map1[k] if map1[k]==map2[k] else 0, k) for k in map1.keys()]
part1.sort()
print("Part 1:", part1[-1])

part2 = 0
for i in range(xmin, xmax):
    for j in range (ymin, ymax):
        part2 += int(sum(abs(x - i) + abs(y - j) for x, y in Cs) < 10000)
print("Part 2:", part2) 