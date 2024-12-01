from utils import get_two_parts, parse_nums

board, moves = get_two_parts(2022, 5)
board = board.splitlines()
stacks = [[] for _ in range(max([int(x) for x in board[-1].split()]))]
for row in board[::-1][1:]:
    for i, z in enumerate(row[1::4]):
        if z.isupper():
            stacks[i].append(z)
            print(str(i) + "," + z)

moves = [parse_nums(line) for line in moves.splitlines()]
PART = 2
for qty, src, to in moves:
    src, to = src - 1, to - 1
    if PART == 1:
        for _ in range(qty):
            to_move = stacks[src].pop()
            stacks[to].extend(to_move)
    elif PART == 2:
        to_move = []
        for _ in range(qty):
            to_move.append(stacks[src].pop())
        stacks[to].extend(to_move[::-1])

print("".join(s[-1] for s in stacks))
