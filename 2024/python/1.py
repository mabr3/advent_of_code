from utils import timer, reader
import sys
from collections import Counter


@timer
def part1(lines):
    l1, l2 = [], []
    for line in lines:
        a, b = line.split()
        l1.append(int(a))
        l2.append(int(b))

    l1.sort()
    l2.sort()
    RESULT = sum([abs(l2[r] - l1[r]) for r in range(len(l1))])
    return RESULT


@timer
def part2(lines):
    l1, l2 = [], []
    for line in lines:
        a, b = line.split()
        l1.append(int(a))
        l2.append(int(b))

    l2_counter = Counter(l2)
    RESULT = sum([l1[r] * l2_counter.get(l1[r], 0) for r in range(len(l1))])
    return RESULT


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = ["3   4", "4   3", "2   5", "1   3", "3   9", "3   3"]
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
