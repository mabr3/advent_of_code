from utils import timer, reader
import sys


@timer
def part1(lines):
    lines = [list(map(int, line.split())) for line in lines]

    def get_sum(line):
        new_line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        if all(j == 0 for j in new_line):
            return 0
        else:
            return new_line[-1] + get_sum(new_line)

    vals = [line[-1] + get_sum(line) for line in lines]
    return sum(vals)


@timer
def part2(lines):
    lines = [list(map(int, line.split())) for line in lines]

    def get_diff(line):
        new_line = [line[i + 1] - line[i] for i in range(len(line) - 1)]
        if all(j == 0 for j in new_line):
            return 0
        else:
            return new_line[0] - get_diff(new_line)

    vals = [line[0] - get_diff(line) for line in lines]
    return sum(vals)


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        lines1 = ["0 3 6 9 12 15", "1 3 6 10 15 21", "10 13 16 21 30 45"]
        part1(lines1)
        lines2 = lines1
        part2(lines2)
