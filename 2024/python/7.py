from utils import timer, reader
import sys


@timer
def part1(lines):
    RESULT = 0
    entries = {}
    for line in lines:
        line_split = line.split(": ")
        print(line_split)
        entries[int(line_split[0])] = [int(i) for i in line_split[1].split()]

    for entry in entries:
        print(entry)
        print(entries[entry])
    print(entries)

    return RESULT


@timer
def part2(lines):
    RESULT = 0
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
            "190: 10 19",
            "3267: 81 40 27",
            "83: 17 5",
            "156: 15 6",
            "7290: 6 8 6 15",
            "161011: 16 10 13",
            "192: 17 8 14",
            "21037: 9 7 18 13",
            "292: 11 6 16 20",
        ]
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
