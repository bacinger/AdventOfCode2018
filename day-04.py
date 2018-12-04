from collections import defaultdict

def getTime(i):
    el = i.split()
    return el[1][3:-1]

def getAction(i):
    el = i.split()
    return el[2]

def getGuard(i):
    el = i.split()
    return el[3][1:]

fname = 'input/day-04.txt'
pattern = defaultdict(list)
hours = defaultdict(int)
with open(fname) as f:
    content = f.read().splitlines()
content.sort()

id = None
sleep = None
for val in content:
    action = getAction(val)
    if action == 'Guard':
        id = getGuard(val)
    elif action == 'falls':
        sleep = int(getTime(val))
    elif action == 'wakes':
        time = int(getTime(val))
        pattern[id].append([sleep, time])

maxsleep = 0
maxguard = None
for guard in pattern:
    sleep = 0
    sleeps = pattern[guard]
    for time in sleeps:
        sleep += time[1] - time[0]
        for t in range(time[0], time[1]):
            hours[(guard, t)] += 1
    if sleep > maxsleep:
        maxsleep = sleep
        maxguard = guard

maxval = 0
maxminute = 0
maxoverall = 0
part2 = None
for t in hours:
    if t[0] == maxguard:
        if hours[t] > maxval:
            maxval = hours[t]
            maxminute = t[1]
    if hours[t] > maxoverall:
        maxoverall = hours[t]
        part2 = t

print("Part 1:", maxguard, maxminute, int(maxguard)*int(maxminute))
print("Part 2:", part2, int(part2[0])*int(part2[1]))