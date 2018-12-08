# Hints from a Reddit thread inspired my final solution because I was unable to solve it on my own as I kept hitting the wall:
# 'RecursionError: maximum recursion depth exceeded in comparison'

fname = 'input/day-08.txt'
with open(fname) as f:
    content = f.read().splitlines()
    for val in content:
        data = [int(x) for x in val.split()]

def sumMetadata(data):
    nr_nodes = data[0]
    nr_metadata = data[1]
    data = data[2:]
    scores = []
    totals = 0

    for i in range(nr_nodes):
        total, score, data = sumMetadata(data)
        totals += total
        scores.append(score)

    totals += sum(data[:nr_metadata])

    if nr_nodes == 0:
        return (totals, sum(data[:nr_metadata]), data[nr_metadata:])
    else:
        return (
            totals,
            sum(scores[k - 1] for k in data[:nr_metadata] if k > 0 and k <= len(scores)),
            data[nr_metadata:]
        )

total, value, remaining = sumMetadata(data)

print('Part 1:', total)
print('Part 2:', value)