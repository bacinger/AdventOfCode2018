def iterate(content, sum, freq):
    for val in content:
        sum += int(val)
        if sum in freq:
            print("Part 2:", sum)
            break
        freq.add(sum)
    return sum

fname = 'input/day-01.txt'
part1 = 0
part2 = 0
freq = {0}

with open(fname) as f:
    content = f.read().splitlines()

for _ in range(150):
    part1 = iterate(content, part1, freq)
    if _ == 0:
        print("Part 1:", part1)