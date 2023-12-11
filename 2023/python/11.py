from utils import timer, reader
import re
import sys


def get_dist(a ,b, cols, lines, expansion_factor):
    dist = abs(a[0]-b[0]) + abs(a[1]-b[1])
    dist += (len([i for i in range(b[0], a[0]) if i in lines]) if a[0]>b[0] else len([i for i in range(a[0], b[0]) if i in lines])) * max(1,expansion_factor-1)
    dist += (len([i for i in range(b[1], a[1]) if i in cols])if a[1]>b[1] else len([i for i in range(a[1], b[1]) if i in cols])) * max(1,expansion_factor-1)
    return dist

@timer
def part1(lines):
    lines = [list(line) for line in lines]
    galaxies = []
    lines_dot, cols_not_dot = set(), set()
    for i in range(len(lines)):
        if '#' in lines[i]:
            for j in range(len(lines[i])):
                if lines[i][j] == '#':
                    galaxies.append((i,j))
                    cols_not_dot.add(j)
        else:
            lines_dot.add(i)
    cols_dot = set([i for i in range(len(lines[0])) if i not in cols_not_dot])
    galaxies_dist = []

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            galaxies_dist.append(get_dist(galaxies[i], galaxies[j], cols_dot, lines_dot,1))

    return sum(galaxies_dist)

@timer
def part2(lines):
    lines = [list(line) for line in lines]
    galaxies = []
    lines_dot, cols_not_dot = set(), set()
    for i in range(len(lines)):
        if '#' in lines[i]:
            for j in range(len(lines[i])):
                if lines[i][j] == '#':
                    galaxies.append((i,j))
                    cols_not_dot.add(j)
        else:
            lines_dot.add(i)
    cols_dot = set([i for i in range(len(lines[0])) if i not in cols_not_dot])
    galaxies_dist = []

    for i in range(len(galaxies)):
        for j in range(i+1, len(galaxies)):
            galaxies_dist.append(get_dist(galaxies[i], galaxies[j], cols_dot, lines_dot,1000000))

    return sum(galaxies_dist)


if __name__=='__main__':
    TEST = False if len(sys.argv) <2 else True
    #TEST = True
    
    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        lines1 = [
            '...#......',
            '.......#..',
            '#.........',
            '..........',
            '......#...',
            '.#........',
            '.........#',
            '..........',
            '.......#..',
            '#...#.....']
        part1(lines1)
        lines2 = [
            "...#......",
            "..........",
            "...#......"]
        part1(lines2)