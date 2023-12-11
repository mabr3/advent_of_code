from utils import timer, reader
import re
import sys

@timer
def part1(lines):
    RESULT = 0
    return RESULT

@timer
def part2(lines):
    RESULT = 0
    return RESULT


if __name__=='__main__':
    TEST = False if len(sys.argv) <2 else True
    
    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        lines1 = [
            '...#......'
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
        lines2 = ["test2"]
        part2(lines2)