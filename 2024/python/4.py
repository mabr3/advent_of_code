from utils import timer, reader
import sys


def check(word: str) -> int:
    return 1 if word == "XMAS" else 0


def construct_word(m, i, j, dir):
    w = []
    for r in range(4):
        w.append(m[i + r * dir[0]][j + r * dir[1]])
    return "".join(w)


@timer
def part1(lines):
    m = [list(line) for line in lines]
    length, width = len(lines), len(lines[0])
    words = []
    directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
    directions["upl"] = tuple(sum(x) for x in zip(directions["up"], directions["left"]))
    directions["upr"] = tuple(
        sum(x) for x in zip(directions["up"], directions["right"])
    )
    directions["downl"] = tuple(
        sum(x) for x in zip(directions["down"], directions["left"])
    )
    directions["downr"] = tuple(
        sum(x) for x in zip(directions["down"], directions["right"])
    )

    for i in range(length):
        for j in range(width):
            # it always starts with X
            if m[i][j] == "X":
                # Check up, upl, upr
                if i >= 3:
                    words.append(construct_word(m, i, j, directions["up"]))
                    if j >= 3:
                        words.append(construct_word(m, i, j, directions["upl"]))
                    if j < width - 3:
                        words.append(construct_word(m, i, j, directions["upr"]))

                # Check down, downl, downr
                if i < length - 3:
                    words.append(construct_word(m, i, j, directions["down"]))
                    if j >= 3:
                        words.append(construct_word(m, i, j, directions["downl"]))
                    if j < width - 3:
                        words.append(construct_word(m, i, j, directions["downr"]))

                # Check left
                if j >= 3:
                    words.append(construct_word(m, i, j, directions["left"]))
                # Check right
                if j < width - 3:
                    words.append(construct_word(m, i, j, directions["right"]))

    RESULT = len([i for i in words if i == "XMAS"])
    return RESULT


@timer
def part2(lines):
    m = [list(line) for line in lines]
    length, width = len(lines), len(lines[0])
    RESULT = 0
    for i in range(1, length - 1):
        for j in range(1, width - 1):
            # it always starts with X
            if m[i][j] == "A":
                if set((m[i - 1][j - 1], m[i + 1][j + 1])) == set(("M", "S")) and \
                    set((m[i - 1][j + 1], m[i + 1][j - 1])) == set(("M", "S")):
                    RESULT += 1

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
            "MMMSXXMASM",
            "MSAMXMSMSA",
            "AMXSXMAAMM",
            "MSAMASMSMX",
            "XMASAMXAMM",
            "XXAMMXXAMA",
            "SMSMSASXSS",
            "SAXAMASAAA",
            "MAMMMXMMMM",
            "MXMXAXMASX",
        ]
        part1(lines1)
        lines2 = lines1
        part2(lines2)
