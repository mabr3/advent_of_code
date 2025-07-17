from utils import timer, reader
import sys
from functools import cmp_to_key


@timer
def _part1(lines):
    RESULT = 0
    dependencies = {}
    updates = []
    for line in lines:
        if "|" in line:
            vals = line.split("|")
            dependencies[vals[1]] = dependencies.get(vals[1], []) + [vals[0]]
        if "," in line:
            updates.append(line.split(","))
    for update in updates:
        printed = set()
        for r in range(len(update)):
            if update[r] not in dependencies:
                # if it has no dependencies it can be printed
                printed.add(update[r])
            else:
                # vals that are in the update lsit that are dependencies also have to be
                # in the printed list
                current_deps = set(update[r + 1 :]).intersection(
                    set(dependencies[update[r]])
                )
                # if it has dependencies check if they have been printed already:
                if not current_deps.issubset(printed):
                    break
                else:
                    printed.add(update[r])
        if len(printed) == len(update):
            RESULT += int(update[int(len(update) / 2)])
    return RESULT


@timer
def part1(lines):
    RESULT = 0
    dependencies = []
    updates = []
    for line in lines:
        if "|" in line:
            vals = line.split("|")
            dependencies.append(vals)
        if "," in line:
            updates.append(line.split(","))

    def comparer(a, b):
        return -1 if [a, b] in dependencies else 1

    valid_updates = [
        u
        for u in updates
        if sorted(u, key=cmp_to_key(lambda a, b: -([a, b] in dependencies))) == u
    ]
    RESULT = sum([int(u[int(len(u) / 2)]) for u in valid_updates])
    return RESULT


@timer
def part2(lines):
    RESULT = 0
    dependencies = []
    updates = []
    for line in lines:
        if "|" in line:
            dependencies.append(line)
        if "," in line:
            updates.append(line.split(","))

    def comparer(a, b):
        return -1 if a + "|" + b in dependencies else 1

    valid_updates = [
        u
        for u in updates
        if not sorted(u, key=cmp_to_key(lambda a, b: -(a + "|" + b in dependencies)))
        == u
    ]
    valid_updates = [sorted(u, key=cmp_to_key(comparer)) for u in valid_updates]
    RESULT = sum([int(u[int(len(u) / 2)]) for u in valid_updates])
    return RESULT


@timer
def xx(lines):
    rules, pages = (
        open("/Users/mike/Desktop/advent_of_code/2024/inputs/5.txt")
        .read()
        .split("\n\n")
    )
    cmp = cmp_to_key(lambda x, y: -(x + "|" + y in rules))

    a = [0, 0]
    for p in pages.split():
        p = p.split(",")
        s = sorted(p, key=cmp)
        a[p != s] += int(s[len(s) // 2])

    print(*a)


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        _part1(lines)
        part1(lines)
        part2(lines)
        xx(lines)
    else:
        print("Testing!")
        lines1 = [
            "47|53",
            "97|13",
            "97|61",
            "97|47",
            "75|29",
            "61|13",
            "75|53",
            "29|13",
            "97|29",
            "53|29",
            "61|53",
            "97|53",
            "61|29",
            "47|13",
            "75|47",
            "97|75",
            "47|61",
            "75|61",
            "47|29",
            "75|13",
            "53|13",
            "",
            "75,47,61,53,29",
            "97,61,53,29,13",
            "75,29,13",
            "75,97,47,61,53",
            "61,13,29",
            "97,13,75,29,47",
        ]
        _part1(lines1)
        part1(lines1)
        lines2 = lines1
        part2(lines2)
        xx(lines1)
