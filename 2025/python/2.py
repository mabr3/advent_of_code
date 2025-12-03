from utils import timer, reader
import sys
import re
import math


@timer
def part1(lines):
    res = 0
    id_ranges = lines[0].split(",")
    for id_ in id_ranges:
        first, last = id_.split("-")
        for num in range(int(first), int(last) + 1):
            n = str(num)
            n_digits = len(n)
            if n_digits % 2 != 0:
                continue
            if n[: n_digits // 2] == n[n_digits // 2 :]:
                res += num
    return res


@timer
def part2(lines):
    res = 0
    id_ranges = lines[0].split(",")
    for id_ in id_ranges:
        first, last = id_.split("-")
        for num in range(int(first), int(last) + 1):
            n = str(num)
            n_digits = len(n)
            if n_digits % 2 != 0:
                continue
            for r in range(1, n_digits // 2 + 1):
                arr = [int(n[i : i + r]) for i in range(0, len(n), r)]
                if len(set(arr)) == 1:
                    res += num
                    break
    return res


@timer
def part1_regex(lines):
    res = 0
    pattern = re.compile(r"(.+)\1$")
    id_ranges = lines[0].split(",")
    for id_ in id_ranges:
        first, last = id_.split("-")
        for num in range(int(first), int(last) + 1):
            if re.match(pattern, str(num)):
                res += num
    return res


@timer
def part2_regex(lines):
    res = 0
    pattern = re.compile(r"(.+)\1+$")
    id_ranges = lines[0].split(",")
    for id_ in id_ranges:
        first, last = id_.split("-")
        for num in range(int(first), int(last) + 1):
            if re.match(pattern, str(num)):
                res += num
    return res


@timer
def part1_logs(lines):
    res = 0
    id_ranges = lines[0].split(",")
    for id_ in id_ranges:
        first, last = id_.split("-")
        for num in range(int(first), int(last) + 1):
            n_digits = int(math.log10(num)) + 1
            if n_digits % 2 != 0:
                continue
            denom = math.pow(10, n_digits / 2)
            # if left side == right side
            if int(num / denom) == num % denom:
                res += num
    return res


@timer
def part2_logs(lines):
    res = 0
    id_ranges = lines[0].split(",")
    for id_ in id_ranges:
        first, last = id_.split("-")
        for num in range(int(first), int(last) + 1):
            n_digits = int(math.log10(num)) + 1
            if n_digits % 2 != 0:
                continue
            denom = math.pow(10, n_digits / 2)
            # if left side == right side
            if int(num / denom) == num % denom:
                res += num
    return res


@timer
def part1_series(lines):
    res = 0
    return res


@timer
def part2_series(lines):
    res = 0
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
        part1_regex(lines)
        part2_regex(lines)
        part1_logs(lines)
        part2_logs(lines)
        part1_series(lines)
        part2_series(lines)
    else:
        print("Testing!")
        lines1 = [
            """11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124"""
        ]
        part1(lines1)
        lines2 = lines1
        part2(lines2)
