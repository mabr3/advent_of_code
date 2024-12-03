from utils import timer, reader
import sys


@timer
def part1(lines):
    levels = []
    RESULT = 0
    for line in lines:
        levels.append([int(i) for i in line.split()])
    for level in levels:
        dir = level[0] > level[1]
        for r in range(1, len(level)):
            diff = abs(level[r - 1] - level[r])
            dir_diff = (level[r - 1] > level[r]) == dir
            if diff == 0 or diff > 3 or not dir_diff:
                break
            if r == len(level) - 1:
                RESULT += 1

    return RESULT


def check_conditions(level, dir):
    for r in range(1, len(level)):
        diff = abs(level[r - 1] - level[r])
        dir_diff = (level[r - 1] > level[r]) == dir
        if diff == 0 or diff > 3 or not dir_diff:
            return r
    return -1


@timer
def part2(lines):
    levels = []
    RESULT = 0
    for line in lines:
        levels.append([int(i) for i in line.split()])
    for level in levels:
        print(f"level: {level}")
        dampener = 0
        dir = level[0] > level[1]
        ind = 0
        while True:
            ind = check_conditions(level[:ind] + level[ind:], dir)
            if ind == -1:
                RESULT += 1
                break
            elif dampener:
                break
            else:
                dampener = True

    return RESULT


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9",
            "9 2 3 4 5",
            "1 9 3 4 5",
            "1 2 9 4 5",
            "1 2 3 9 5",
            "1 2 3 4 9",
            "3 2 3 4 5",
        ]
        part1(lines1)
        lines2 = [
            "7 6 4 2 1",
            "1 2 7 8 9",
            "9 7 6 2 1",
            "1 3 2 4 5",
            "8 6 4 4 1",
            "1 3 6 7 9",
        ]
        part2(lines2)
