from utils import timer, reader
import sys


@timer
def part1(lines):
    sum_chrs = []
    for line in lines:
        print(line)
        sum_chrs.append(len(line))
    print(sum_chrs)
    print(sum(sum_chrs))
    RESULT = 0
    return RESULT


@timer
def part2(lines):
    RESULT = 0
    return RESULT


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = ['""',
                  '"abc"',
                  '"aaa\"aaa"',
                  '"\x27"']
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
