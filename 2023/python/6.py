from utils import timer, reader
import re
import sys
from functools import reduce

@timer
def part1(lines):
    times = [int(i.group()) for i in re.finditer(r'(\d+)', lines[0])]
    distances = [int(i.group()) for i in re.finditer(r'(\d+)', lines[1])]
    counts = [times[i] - 1 - 2*int((-times[i]*-1.0 - (times[i]*times[i] -4*1.0*distances[i])**0.5)/(2*1.0)) for i in range(len(times))]
    res = reduce(lambda x,y: x*y, counts)
    return res

@timer
def part2(lines):
    time = int(''.join([i.group() for i in re.finditer(r'(\d+)', lines[0])]))
    distance = int(''.join([i.group() for i in re.finditer(r'(\d+)', lines[1])]))
    a = 1.0
    b = -time*1.0 
    c = distance*1.0
    v1 = int((-b - (b*b -4*a*c)**0.5)/(2*a))
    return time-v1-v1-1


if __name__=='__main__':
    TEST = False if len(sys.argv) <2 else True
    
    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        lines1 = ['Time:      7  15   30',
        'Distance:  9  40  200']
        part1(lines1)
        lines2 = lines1
        part2(lines2)