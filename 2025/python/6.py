from utils import timer, reader
from functools import reduce
import sys


@timer
def part1(lines):
    res = 0
    ops = lines[-1].split()
    results = [0 if op == "+" else 1 for op in ops]
    for line in lines[:-1]:
        nums = [int(n) for n in line.split()]
        for i, num in enumerate(nums):
            if ops[i] == "+":
                results[i] += num
            else:
                results[i] *= num
    res = sum(results)
    return res


@timer
def part2(lines):
    res = 0
    ops = [(i,v) for i, v in enumerate(list(lines[-1])) if v != " "]
    # transpose lines:
    lines_t = [["" for _ in range(len(lines) - 1)] for j in range(len(lines[0]))]
    for i in range(len(lines) - 1):
        for j in range(len(lines[0])):
            lines_t[j][i] = lines[i][j]
    print(len(lines_t))
    print(len(lines_t[0]))
    print(lines_t)
    for i in range(len(ops)):
        beg = ops[i][0]
        end = ops[i+1][0]-1 if i < len(ops)-1 else len(lines[0])
        vals = [int(''.join(lines_t[j])) for j in range(beg, end)]
        if ops[i][1] == '+':
            result = reduce(lambda x,y: x+y, vals)
        else:
            result = reduce(lambda x,y: x*y, vals)
        res += result


    # for line[::-1] in lines:
    #     idx = len(ops)-1
    #     for r in range(len(line)-1, 0, -1):
    #         if r > ops[idx][0]:
    #             nums[idx] += line[r] if line[r] != ''
    #         elif
    # probably can use module

    print(ops)
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = [
            "123 328  51 64 ",
            " 45 64  387 23 ",
            "  6 98  215 314",
            "*   +   *   + ",
        ]
        assert part1(lines1) == 4277556, "should be 4277556"
        lines2 = lines1
        assert part2(lines2) == 3263827, "should be 3263827"
