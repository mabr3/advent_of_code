from utils import timer, reader
import sys


@timer
def part1(lines):
    res = 0
    return res


@timer
def part2(lines):
    res = 0
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
