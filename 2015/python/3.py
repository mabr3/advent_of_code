from utils import timer, reader
import sys


@timer
def part1(lines):
    houses = {}
    i, j = 0, 0
    houses[(i, j)] = houses.get((i, j), 0) + 1
    for dir in lines[0]:
        if dir == '^':
            i -= 1
        elif dir == 'v':
            i += 1
        elif dir == '<':
            j -= 1
        elif dir == '>':
            j += 1
        houses[(i, j)] = houses.get((i, j), 0) + 1
    RESULT = len(houses.keys())
    return RESULT


@timer
def part2(lines):
    houses = {}
    i, j = 0, 0
    ii, jj = 0, 0
    houses[(i, j)] = houses.get((i, j), 0) + 1
    for e, dir in enumerate(lines[0]):
        step = (0, 0)

        if dir == '^':
            step = (-1, 0)
        elif dir == 'v':
            step = (1, 0)
        elif dir == '<':
            step = (0, -1)
        elif dir == '>':
            step = (0, 1)
        if e % 2 == 0:
            i, j = i + step[0], j + step[1]
            houses[(i, j)] = houses.get((i, j), 0) + 1
        else:
            ii, jj = ii + step[0], jj + step[1]
            houses[(ii, jj)] = houses.get((ii, jj), 0) + 1

    RESULT = len(houses.keys())
    return RESULT


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = ['^>v<']
        part1(lines1)
        lines2 = ["^v"]
        part2(lines2)
