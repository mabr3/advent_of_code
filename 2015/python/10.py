from utils import timer, reader
import sys


def do_processing(line: str) -> str:
    previous = None
    res = ''
    c = 0
    for ch in line:
        if ch != previous:
            if previous:
                res += f"{c}{previous}"
            c = 1
            previous = ch
        else:
            c += 1

    res += f"{c}{previous}"
    return res


@timer
def part1(lines):
    line = lines[0]
    for _ in range(40):
        line = do_processing(line)

    RESULT = len(line)
    return RESULT


@timer
def part2(lines):
    line = lines[0]
    for _ in range(50):
        line = do_processing(line)

    RESULT = len(line)
    return RESULT


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = ['111221']
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
