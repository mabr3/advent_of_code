from utils import timer, reader
import sys
import re


@timer
def part1(lines):
    RESULT = 0
    pattern = re.compile(r"mul\((?P<left>\d+),(?P<right>\d+)\)")
    for line in lines:
        vals = re.findall(pattern, line)
        RESULT += sum(int(a[0]) * int(a[1]) for a in vals)
    return RESULT


@timer
def part2(lines):
    RESULT = 0
    pattern = re.compile(r"(don't)|(do(?!n't))|mul\((\d+),(\d+)\)")
    flag = True
    for line in lines:
        vals = re.findall(pattern, line)
        for v1,v2,v3,v4 in vals:
            if v1 or v2:
                flag = bool(v2)
            else:
                RESULT += flag * (int(v3) * int(v4))

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
            "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
        ]
        part1(lines1)
        lines2 = [
            "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
        ]
        part2(lines2)
