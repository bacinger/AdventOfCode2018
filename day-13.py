import re

with open('input/day-13.txt') as f:
    val = [line.rstrip('\n') for line in f]
    track = [line.replace('>', '-').replace('<', '-').replace('^', '|').replace('v', '|') for line in val]
    carts = []
    for x, line in enumerate(val):
        for pos in re.finditer(r'[<>v\^]', line):
            carts.append((x, pos.start(), pos.group(0), 0))

    firstCrash = False
    while True:
        crashed = set()
        for i in range(len(carts)):
            # x, y - coordinates
            # c - character on map
            # m - movement order
            (x, y, c, m) = carts[i]
            if (x, y) in crashed:
                continue
            if c == '>':
                n = (x, y + 1)
            elif c == '<':
                n = (x, y - 1)
            elif c == '^':
                n = (x - 1, y)
            elif c == 'v':
                n = (x + 1, y)
            (nx, ny) = n
            if any(ax == nx and ay == ny for (ax, ay, ac, am) in carts):
                if not firstCrash:
                    print('Part 1:', (ny, nx))
                    firstCrash = True
                crashed.add(n)
            if track[nx][ny] in '\\/':
                c = {
                    '>\\': 'v',
                    '<\\': '^',
                    '^\\': '<',
                    'v\\': '>',
                    '>/': '^',
                    '</': 'v',
                    '^/': '>',
                    'v/': '<',
                }[c + track[nx][ny]]
            elif track[nx][ny] == '+':
                c = {
                    '>0': '^',
                    '>1': '>',
                    '>2': 'v',
                    '<0': 'v',
                    '<1': '<',
                    '<2': '^',
                    '^0': '<',
                    '^1': '^',
                    '^2': '>',
                    'v0': '>',
                    'v1': 'v',
                    'v2': '<',
                }[c + str(m)]
                m = (m + 1) % 3
            carts[i] = (nx, ny, c, m)
        else:
            carts = [cart for cart in carts if (cart[0], cart[1]) not in crashed]
            if len(carts) == 1:
                print('Part 2:', (carts[0][1], carts[0][0]))
                break
            carts.sort()
            continue
        break