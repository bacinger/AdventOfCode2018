import re
import numpy as np
from collections import defaultdict

fname = 'input/day-10.txt'
with open(fname) as f:
    content = f.read().splitlines()
    input = np.array([[int(i) for i in re.findall(r'-?\d+', l)] for l in content])

bbox = defaultdict(int)
for i in range(40000):
    min_x = min(x + i * vx for (x, y, vx, vy) in input)
    max_x = max(x + i * vx for (x, y, vx, vy) in input)
    min_y = min(y + i * vy for (x, y, vx, vy) in input)
    max_y = max(y + i * vy for (x, y, vx, vy) in input)
    bbox[i] = max_x - min_x + max_y - min_y
bbox_min = min(bbox, key=bbox.get)

bbox_x = max(x + bbox_min * vx for (x, y, vx, vy) in input) + 1
bbox_y = max(y + bbox_min * vy for (x, y, vx, vy) in input) + 1

input[:,:2] += bbox_min * input[:,2:]
input[:,0] -= input[:,0].min()
input[:,1] -= input[:,1].min()

sky = np.zeros((bbox_y, bbox_x),dtype=int)
for i in range(len(input)):
    sky[input[i,1], input[i,0]] = 1

print('Part 1:')
for i in range(bbox_y):
    print(''.join('#' if p else ' ' for p in sky[i]))

print('Part 2:', bbox_min)