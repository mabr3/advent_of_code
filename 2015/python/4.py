from utils import timer, reader
import sys
import hashlib


@timer
def part1(lines):
    # brute force

    target = '00000'
    text = lines[0]
    n = 0
    while hashlib.md5(
            (str(text) + str(n)).encode('ascii')).hexdigest()[:5] != target:
        n += 1

    return n


@timer
def part2(lines):
    # brute force

    target = '000000'
    text = lines[0]
    n = 0
    while hashlib.md5(
            (str(text) + str(n)).encode('ascii')).hexdigest()[:6] != target:
        n += 1

    return n


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = ['abcdef']
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
