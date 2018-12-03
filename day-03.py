import re
from collections import defaultdict

fname = 'input/day-03.txt'
with open(fname) as f:
    content = f.read().splitlines()

elfs = map(lambda l: map(int, re.findall(r'-?\d+', l)), content)
fabric = defaultdict(list)
overlaps = {}
for (cnr, x, y, width, height) in elfs:
  overlaps[cnr] = set()
  for i in range(x, x + width):
    for j in range(y, y + height):
      if fabric[(i,j)]:
        for nr in fabric[(i, j)]:
          overlaps[nr].add(cnr)
          overlaps[cnr].add(nr)
      fabric[(i,j)].append(cnr)

print("Part 1:", len([pt1 for pt1 in fabric if len(fabric[pt1]) > 1]))
print("Part 2:", [pt2 for pt2 in overlaps if len(overlaps[pt2]) == 0][0])