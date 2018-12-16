serial_number = 5791

"""
1. Find the fuel cell's rack ID, which is its X coordinate plus 10.
2. Begin with a power level of the rack ID times the Y coordinate.
3. Increase the power level by the value of the grid serial number (your puzzle input).
4. Set the power level to itself multiplied by the rack ID.
5. Keep only the hundreds digit of the power level (so 12345 becomes 3; numbers with no hundreds digit become 0).
6. Subtract 5 from the power level.
"""
def calc(x, y, sn):
    rack_ID = x + 10
    power_level = (rack_ID * y + sn) * rack_ID
    hundreds = int(str(power_level)[-3])
    return hundreds - 5

a = []
for i in range(300):
    a.append([])
    for j in range(300):
        a[i].append(calc(i, j, serial_number))

total_power = 0
max_power = 0
max_power_pos = (0,0)
for i in range(298):
    for j in range(298):
        total_power = a[i][j]+a[i+1][j]+a[i+2][j]+a[i][j+1]+a[i+1][j+1]+a[i+2][j+1]+a[i][j+2]+a[i+1][j+2]+a[i+2][j+2]
        if total_power > max_power:
            max_power = total_power
            max_power_pos = (i, j)

print('Part 1:', max_power_pos, max_power)

size = 50 # Size can be 1:300, but 50 is enough
total_power = 0
max_power = 0
max_power_pos = (0,0)
max_size = 1
for i in range(300):
    for j in range(300):
        for s in range(size):
            for x in range(s+1):
                for y in range(s+1):
                    if (i+x < 300) and (j+y < 300):
                        total_power += a[i+x][j+y]
                    else:
                        break
            if total_power > max_power:
                max_power = total_power
                max_power_pos = (i, j)
                max_size = s+1
            total_power = 0

print('Part 2:', max_power_pos, max_size, max_power)