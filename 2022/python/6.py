from utils import get_lines

lines = get_lines(2022, 6)
for line in lines:
    # P1
    for r in range(3, len(line)):
        if len(list(set(line[r - 4 : r]))) == 4:
            print(r)
            break
    # P2
    for r in range(13, len(line)):
        if len(list(set(line[r - 14 : r]))) == 14:
            print(r)
            break
