from utils import timer, reader
import sys

@timer
def part1(lines):
    _map = []
    guard = (None,None)
    length, width = len(lines), len(lines[0])
    for i,line in enumerate(lines):
        _map.append([i for i in line])
        if '^' in line:
            guard = (i, line.index('^'))
    #just moving around
    RESULT = 1
    directions = [(-1,0), (0, 1), (1,0), (0,-1)]
    dir_index = 0
    def check_bounds(guard, length, width) -> bool:
        return (0 <= guard[0] < length) and (0 <= guard[1] < width)
    # while the guard is still in bounds
    while True:
        new_guard = (guard[0] + directions[dir_index][0],
                    guard[1] + directions[dir_index][1])
        if not check_bounds(new_guard, length, width):
            #guard whent out of bounds. break
            break
        elif _map[new_guard[0]][new_guard[1]] == '#':
            dir_index = (dir_index + 1) % 4
        else:
            if _map[new_guard[0]][new_guard[1]] == '.':
                _map[new_guard[0]][new_guard[1]] = 'X'
                RESULT += 1
            guard = new_guard
    return RESULT


@timer
def part2(lines):
    # _map = []
    # guard = (None,None)
    # length, width = len(lines), len(lines[0])
    # pattern = re.compile(r'#')
    # obstacles = {}
    # def check_bounds(guard, length, width) -> bool:
    #     return (0 <= guard[0] < length) and (0 <= guard[1] < width)
    # for i,line in enumerate(lines):
    #     obstacles[i] = [i.start() for i in re.finditer(pattern, line)]
    #     if '^' in line:
    #         guard = (i, line.index('^'))
    #
    # while True:
    #
    #
    #just moving around
    RESULT = 0
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
            "....#.....",
            ".........#",
            "..........",
            "..#.......",
            ".......#..",
            "..........",
            ".#..^.....",
            "........#.",
            "#.........",
            "......#...",
        ]
        part1(lines1)
        lines2 = lines1
        part2(lines2)
