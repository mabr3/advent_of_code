from utils import timer, reader
import sys


@timer
def part1(lines):
    RESULT = 0
    pointer = 50
    length = 100
    for line in lines:
        direction = -1 if line[0] == "L" else 1
        rotation = int(line[1:])
        new_pointer = pointer + direction * rotation
        pointer = new_pointer % length
        if pointer == 0:
            RESULT += 1
    return RESULT


@timer
def part2(lines):
    res = 0
    pointer = 50
    length = 100
    # DO ALL CLICKS
    for line in lines:
        direction = -1 if line[0] == "L" else 1
        rotation = int(line[1:])
        for r in range(0, rotation):
            pointer += direction  # CLICK
            if pointer > 99 or pointer < 0:
                pointer = pointer % length
            if pointer == 0:
                res += 1

    # for l in lines:
    #     direction = -1 if l[0] == "L" else 1
    #     rotation = int(l[1:])
    #     if rotation ==0:
    #         continue
    #     new_pointer = pointer + direction * rotation
    #     d, m = divmod(new_pointer, length)
    #     print(f"The dial is rotated {l} to point at {new_pointer} -> {pointer}")
    #     print(f"divmod({new_pointer}, {length}) = ({d}, {m})")
    #     if new_pointer < 0 and d != 0:
    #         res += abs(d) -1
    #     else:
    #         res += abs(d)
    #     if m == 0:
    #         res +=1
    #     pointer = m
    #     print(f"counter is {res}")
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        # lines1 = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        # part1(lines1)
        lines2 = ["L68", "L30", "R48", "L5", "R60", "L55", "L1", "L99", "R14", "L82"]
        part2(lines2)
        # lines3 = ["R1000"]
        # part2(lines3)
        # lines4 = ["L250"]
        # part2(lines4)
        # lines5 = ["R250"]
        # part2(lines5)
        # lines6 = ["R50", "R100", "L100", "L1000"]
        # part2(lines6)
