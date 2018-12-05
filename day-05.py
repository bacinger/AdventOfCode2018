from string import ascii_lowercase

def analyze(str):    
    i = 0
    b = None
    looping = True
    while looping:
        c = str[i]
        if b == None:
            b = c
        else:
            if b != c and b.lower() == c.lower():
                if str[i-1:i+1] == b + c:
                    str = str[:i-1] + str[i+1:]
                i = 0
            b = c
        i += 1
        if i == len(str):
            looping = False
    return str

fname = 'input/day-05.txt'
with open(fname) as f:
    content = f.read().splitlines()

for val in content:
    #val = 'dabAcCaCBAcCcaDA'
    res = analyze(val)
    print("Part 1:", len(res))

    best = len(val)
    for letter in ascii_lowercase:
        reduced = [l for l in val if l != letter and l != letter.upper()]
        res = analyze(''.join(reduced))
        if len(res) < best:
            best = len(res)
    print("Part 2:", best)