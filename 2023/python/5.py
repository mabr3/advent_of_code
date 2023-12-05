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
    seed_ranges = [(range(int(i[0]), int(i[0])+int(i[1]))) for i in [i.split() for i in re.findall(r'(\d+\s\d+)',lines[0])]]
    lines = lines[3:]
    k=0
    # for each block, calculate the ranges
    # each range might result in more ranges
    # each range either is out of the block range
    # or fully inside, or to the left or to the right
    # in these last 2 cases, new ranges must be added to still be processed.

    #ideally if there are equal values we could re-use...
    while k < len(lines):
        if not lines[k] or 'map' in lines[k]:
            k+=1
        else:
            # get all entries in a block
            block = []
            while k< len(lines) and lines[k] != '':
                block.append([int(i.group()) for i in re.finditer(r'(\d+)', lines[k])])
                k+=1 
            sr=0
            processed = [0]* len(seed_ranges)
            while sr < len(seed_ranges):
                r_b, r_e = seed_ranges[sr].start, seed_ranges[sr].stop
                for b in block:
                    if processed[sr] != 0:
                        break
                    #Diff from destination range from source range
                    diff = b[0]-b[1]
                    range_b = range(b[1],b[1]+b[2])
                    range_b_b, range_b_e = range_b.start, range_b.stop
                    #Check for intersection:
                    if r_b in range_b or r_e-1 in range_b:
                        #print("INTERSECTION")
                        if r_b >= range_b_b and r_e <= range_b_e:
                            #if it is fully inside:
                            seed_ranges[sr] = range(r_b+diff, r_e+diff)    
                            processed[sr]=1
                        else:
                            # might also be that some ranges are bigger in both sides, hence the ifs and 
                            # not elsif
                            if r_b < range_b_b:
                                #check if it is on the left and add the right part to the list
                                seed_ranges[sr] = range(range_b_b + diff, r_e + diff)
                                processed[sr]=-1
                                seed_ranges.append(range(r_b,  range_b_b))
                                processed.append(0)
                            if r_e > range_b_e:
                                #check if it is on the right and add the right part to the list
                                if processed != -1:
                                    #means left side hasn't been processed already - lazy ik
                                    seed_ranges[sr] = range(r_b + diff, range_b_e + diff)
                                    processed[sr]=1
                                seed_ranges.append(range(range_b_e, r_e))
                                processed.append(0)  
                sr+=1            

    res = min(map(lambda x: min(x), seed_ranges))
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