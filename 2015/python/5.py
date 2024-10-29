from utils import timer, reader
import sys

VOWELS = set(['a', 'e', 'i', 'o', 'u'])
FORBIDDEN = ['ab', 'cd', 'pq', 'xy']


@timer
def part1(lines):
    nice_count = 0

    for line in lines:
        if any(element in line for element in FORBIDDEN):
            continue
        if len([elem for elem in line if elem in VOWELS]) > 2 and \
                any(line[r] == line[r+1] for r in range(len(line)-1)):
            nice_count += 1
    return nice_count


@timer
def part2(lines):
    nice_count = 0

    for line in lines:
        if any([line[i: i+2] in line[i+2:] for i in range(len(line) - 2)]) \
                and \
                any(line[r] == line[r+2] for r in range(len(line)-2)):
            nice_count += 1
    return nice_count


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = ['ugknbfddgicrmopn',
                  'aaa',
                  'jchzalrnumimnmhp',
                  'haegwjzuvuyypxyu',
                  'dvszwmarrgswjxmb'
                  ]
        part1(lines1)
        lines2 = ['qjhvhtzxzqqjkmpb',
                  'xxyxx',
                  'uurcxstgmygtbstg',
                  'ieodomkazucvgmuy']
        part2(lines2)
