from utils import timer, reader
import sys


@timer
def part1(lines):
    res = 0
    shapes = []
    idx = 0
    configs = []
    for i in range(len(lines)):
        line = lines[i]
        if line == "":
            continue
        elif line[-1] == ":":
            idx = int(line[:-1])
            shapes.append([])
            continue
        elif "x" in line:
            splits = line.split(":")
            area = tuple(int(x) for x in splits[0].split("x"))
            presents = [int(x) for x in splits[1].split()]
            configs.append((area, presents))
        else:
            shapes[idx].append(list(line))

    shape_areas = [
        sum(1 if c == "#" else 0 for row in shape for c in row) for shape in shapes
    ]
    for config in configs:
        area = config[0][0] * config[0][1]
        required = sum(c * shape_areas[i] for i, c in enumerate(config[1]))
        if required < area:
            res += 1
    return res


@timer
def part2(lines):
    res = 0
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
            "0:",
            "###",
            "##.",
            "##.",
            "",
            "1:",
            "###",
            "##.",
            ".##",
            "",
            "2:",
            ".##",
            "###",
            "##.",
            "",
            "3:",
            "##.",
            "###",
            "##.",
            "",
            "4:",
            "###",
            "#..",
            "###",
            "",
            "5:",
            "###",
            ".#.",
            "###",
            "",
            "4x4: 0 0 0 0 2 0",
            "12x5: 1 0 1 0 2 2",
            "12x5: 1 0 1 0 3 2",
        ]
        assert part1(lines1) == 2, "should be 2"
        lines2 = ["test2"]
        part2(lines2)
