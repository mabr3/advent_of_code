from utils import timer, reader
import sys


@timer
def part1(lines):

    floor = 0
    for line in lines[0]:
        floor = floor + 1 if line == '(' else floor - 1

    return floor


@timer
def part2(lines):
    floor = 0
    for i, v in enumerate(lines[0]):
        floor = floor + 1 if v == '(' else floor - 1
        if floor == -1:
            break

    return i + 1


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('TESTING')
        lines1 = ['))(((((']
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
