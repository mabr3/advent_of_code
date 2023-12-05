from utils import timer, reader
import re
import sys

@timer
def part1(lines):
    # construct data structures as needed
    seeds = [int(i.group()) for i in re.finditer(r'(\d+)', lines[0])]
    processed = [0]*len(seeds)
    k=1
    while k < len(lines):
        if not lines[k]:
            k+=1
            processed = [0]*len(seeds)
        else:
            d_start, s_start, length =  [int(i.group()) for i in re.finditer(r'(\d+)', lines[k])]
            for sr in range(len(seeds)):
                if processed[sr]==0 and seeds[sr] in range(s_start, s_start+length):
                    seeds[sr] = d_start + (seeds[sr]-s_start)
                    processed[sr] = 1
        k+=1

    res = min(seeds)
    return res

@timer
def part2(lines):
    # construct data structures as needed
    seeds = [int(i.group()) for i in re.finditer(r'(\d+)', lines[0])]
    processed = [0]*len(seeds)
    k=1
    while k < len(lines):
        if not lines[k]:
            k+=1
            processed = [0]*len(seeds)
        else:
            d_start, s_start, length =  [int(i.group()) for i in re.finditer(r'(\d+)', lines[k])]
            for sr in range(len(seeds)):
                if processed[sr]==0 and seeds[sr] in range(s_start, s_start+length):
                    seeds[sr] = d_start + (seeds[sr]-s_start)
                    processed[sr] = 1
        k+=1

    res = min(seeds)
    return res


if __name__=='__main__':
    TEST = False if len(sys.argv) <2 else True
    
    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        lines1 = ['seeds: 79 14 55 13',
                '',
                'seed-to-soil map:',
                "50 98 2",
                "52 50 48",
                "",
                "soil-to-fertilizer map:",
                "0 15 37",
                "37 52 2",
                "39 0 15",
                "",
                "fertilizer-to-water map:",
                "49 53 8",
                "0 11 42",
                "42 0 7",
                "57 7 4",
                "",
                "water-to-light map:",
                "88 18 7",
                "18 25 70",
                "",
                "light-to-temperature map:",
                "45 77 23",
                "81 45 19",
                "68 64 13",
                "",
                "temperature-to-humidity map:",
                "0 69 1",
                "1 0 69",
                "",
                "humidity-to-location map:",
                "60 56 37",
                "56 93 4"]
        part1(lines1)
        lines2 = lines1
        part2(lines2)