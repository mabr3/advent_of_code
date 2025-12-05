from utils import timer, reader
import sys


@timer
def part1(lines):
    res = 0
    for line in lines:
        line_len = len(line)
        line = [int(ll) for ll in line]
        batteries_needed = 2
        batteries = []
        idx = -1
        while batteries_needed > 0:
            arr = line[idx + 1 : line_len - batteries_needed + 1]
            battery = max(arr)
            batteries.append(str(battery))
            batteries_needed -= 1
            idx = line.index(battery, idx + 1)
        res += int("".join(batteries))
    return res


@timer
def part1_2(lines):
    res = 0
    n = 2
    for line in lines:
        bat1, bat2 = line[0], line[1]
        line_len = len(line)
        for r in range(n - 1, line_len):
            # if curent digit is bigger than p1, replace both
            # p1 and p2. but only if we're not at the last digit
            if line[r] > bat1 and r != line_len - 1:
                bat1 = line[r]
                bat2 = line[r + 1]
                r += 1
            elif line[r] > bat2:
                bat2 = line[r]
        res += int(bat1 + bat2)
    return res


@timer
def part2(lines):
    res = 0
    for line in lines:
        line_len = len(line)
        line = [int(ll) for ll in line]
        batteries_needed = 12
        batteries = []
        idx = -1
        while batteries_needed > 0:
            arr = line[idx + 1 : line_len - batteries_needed + 1]
            battery = max(arr)
            batteries.append(str(battery))
            batteries_needed -= 1
            idx = line.index(battery, idx + 1)
        res += int("".join(batteries))
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part1_2(lines)
        part2(lines)

    else:
        print("Testing!")
        lines1 = [
            "987654321111111",
            "811111111111119",
            "234234234234278",
            "818181911112111",
        ]
        part1(lines1)
        lines2 = lines1
        part2(lines2)
