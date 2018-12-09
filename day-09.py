fname = 'input/day-09.txt'
with open(fname) as f:
    content = f.read().splitlines()
    for val in content:
        input = val.split()
        nr_players = int(input[0])
        last_marble = int(input[6])

def parseGame(mul):
    scores = [0] * nr_players
    board = [0]
    current = 0
    player = -1
    for i in range(1, (last_marble*mul) + 1):
        player = (player + 1) % len(scores)
        if i % 23 == 0:
            scores[player] = scores[player] + i
            current = (current - 7) % len(board)
            scores[player] = scores[player] + board.pop(current)
            current = current % len(board)
        else:
            new_pos = (current + 2) % len(board)
            board.insert(new_pos, i)
            current = new_pos
    return max(scores)

print('Part 1:', parseGame(1))
print('Part 2:', parseGame(100)) # Warning: This naive solution for Part 2 is extremely slow and inefficient!