from utils import timer, reader
import sys


@timer
def part1(lines):
    total = 0
    for line in lines:
        l, w, h = [int(v) for v in line.split('x')]
        sides = [l * w,   w * h,  h * l]
        total += 2*sum(sides) + min(sides)

    # 2*l*w + 2*w*h + 2*h*l
    return total


@timer
def part2(lines):
    total = 0
    for line in lines:
        l, w, h = [int(v) for v in line.split('x')]
        sides = sorted([l, w, h])
        total += 2*sum(sides[:2]) + l*w*h

    return total


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = ['1x1x10']
        part1(lines1)
        lines2 = ["1x1x10"]
        part2(lines2)
