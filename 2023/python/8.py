from utils import timer, reader
import re
import sys
from math import lcm


@timer
def part1(lines):
    directions = list(lines[0])
    pattern = r"(\w{3})"
    p_c = re.compile(pattern)
    moves = [p_c.findall(i) for i in lines[2:]]
    moves = {m[0]: {"L": m[1], "R": m[2]} for m in moves}
    dest_key = "AAA"
    c = 0
    while dest_key != "ZZZ":
        dest_key = moves.get(dest_key)[directions[c % len(directions)]]
        c += 1
    return c


@timer
def part2(lines):
    directions = list(lines[0])
    pattern = r"(\w{3})"
    p_c = re.compile(pattern)
    moves = [p_c.findall(i) for i in lines[2:]]
    moves = {m[0]: {"L": m[1], "R": m[2]} for m in moves}
    keys = [i for i in moves.keys() if i[2] == "A"]
    l_k = len(keys)
    counter = 0
    z_found = []
    while len(z_found) != l_k:
        keys = [moves.get(key)[directions[counter % len(directions)]] for key in keys]
        counter += 1
        if any(i[2] == "Z" for i in keys):
            for r in range(len(keys) - 1, -1, -1):
                if keys[r][2] == "Z":
                    z_found.append(counter)
                    del keys[r]

    return lcm(*z_found)


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        lines1 = [
            "RL",
            "",
            "AAA = (BBB, CCC)",
            "BBB = (DDD, EEE)",
            "CCC = (ZZZ, GGG)",
            "DDD = (DDD, DDD)",
            "EEE = (EEE, EEE)",
            "GGG = (GGG, GGG)",
            "ZZZ = (ZZZ, ZZZ)",
        ]
        part1(lines1)
        lines2 = [
            "LR",
            "",
            "11A = (11B, XXX)",
            "11B = (XXX, 11Z)",
            "11Z = (11B, XXX)",
            "22A = (22B, XXX)",
            "22B = (22C, 22C)",
            "22C = (22Z, 22Z)",
            "22Z = (22B, 22B)",
            "XXX = (XXX, XXX)",
        ]
        part2(lines2)
