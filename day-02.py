import itertools

fname = 'day-02.txt'

with open(fname) as f:
    content = f.read().splitlines()

two = 0
three = 0
for val in content:
    dict = {}
    for letter in val:
        if letter not in dict.keys():
            dict[letter] = 1
        else:
            dict[letter] += 1
    for key, value in dict.items():
        if value == 2:
            two += 1
            break
    for key, value in dict.items():
        if value == 3:
            three += 1
            break

print(two, three, int(two)*int(three))

for a, b in itertools.combinations(content, 2):
    rez = [i for i in range(len(a)) if a[i] != b[i]]
    if len(rez) == 1:
        print(a,b)