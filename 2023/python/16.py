from utils import timer, reader
import sys


def do_path(lines, init_coords, init_dir):
    energized = 0
    coords = init_coords
    direction = init_dir

    if (
        lines[coords(0)][coords(1)] == "."
        or (lines[coords(0)][coords(1)] == "|" and direction in [(1, 0), (-1, 0)])
        or (lines[coords(0)][coords(1)] == "-" and direction in [(0, 1), (0, -1)])
    ):
        energized += 1
        coords = (coords(0) + direction(0), coords(1) + direction(1))
    elif lines[coords(0)][coords(1)] == "-" and direction in [(1, 0), (-1, 0)]:
        energized = do_path(lines, coords, 0) + do_path(lines, 0, 0) + 1
    elif lines[coords(0)][coords(1)] == "|" and direction in [(0, 1), (0, -1)]:
        energized = do_path(lines, coords, 0) + do_path(lines, 0, 0) + 1
    elif lines[coords(0)][coords(1)] == "-":
        pass
        #TODO

    return energized


@timer
def part1(lines):
    RESULT = do_path(lines, (0, 0), (0, 1))
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
        lines1 = [
            ".|...\\....",
            "|.-.\\.....",
            ".....|-...",
            "........|.",
            "..........",
            ".........\\",
            "..../.\\\\..",
            ".-.-/..|..",
            ".|....-|.\\",
            "..//.|....",
        ]
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
