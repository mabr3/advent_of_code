from utils import timer, reader
import sys
import re


@timer
def part1(lines):
    n = 1000
    grid = [([False] * n) for _ in range(n)]
    patern = re.compile(r'^(\w.*)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)$')
    for line in lines:
        m = re.match(patern, line)
        action = m.group(1)
        x1, y1 = int(m.group(2)), int(m.group(3))
        x2, y2 = int(m.group(4)), int(m.group(5))
        if action[:4] == 'turn':
            if action[-2:] == 'on':
                v = True
            else:
                v = False
            for c in range(y1, y2+1):
                grid[c][x1:x2+1] = [v] * (x2-x1+1)
        elif action == 'toggle':
            for c in range(y1, y2+1):
                grid[c][x1:x2+1] = [not i for i in grid[c][x1:x2+1]]

    RESULT = sum([i for j in grid for i in j if i])
    return RESULT


@timer
def part2(lines):
    n = 1000
    grid = [([0] * n) for _ in range(n)]
    patern = re.compile(r'^(\w.*)\s(\d+),(\d+)\sthrough\s(\d+),(\d+)$')
    for line in lines:
        m = re.match(patern, line)
        action = m.group(1)
        x1, y1 = int(m.group(2)), int(m.group(3))
        x2, y2 = int(m.group(4)), int(m.group(5))
        if action[:4] == 'turn':
            if action[-2:] == 'on':
                v = 1
            else:
                v = -1
        else:
            v = 2
        for c in range(y1, y2 + 1):
            for r in range(x1, x2 + 1):
                grid[c][r] = max(0, grid[c][r] + v)

    RESULT = sum([i for j in grid for i in j])
    return RESULT


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = ['toggle 0,0 through 9,0']
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
