from utils import timer, reader
import re
import sys
from functools import reduce

@timer
def part1(lines):
    rules = [0, 12, 13, 14]
    pattern = fr"(?<=Game\s)(\d*)|(\d*)(?=\sred)|(\d*)(?=\sgreen)|(\d*)(?=\sblue)"
    p_c = re.compile(pattern=pattern)   
    l_t = [list(zip(*p_c.findall(l))) for l in lines]
    sums =[[max(map(lambda x: int(x) if x.isdigit() else 0, ttt)) for ttt in tt] for tt in l_t] 
    res = sum(list(map(lambda x: x[0] if x[1]<=rules[1] and x[2]<=rules[2] and x[3]<=rules[3] else 0, sums)))
    return res

@timer
def part2(lines):
    rules = [0, 12, 13, 14]
    pattern = fr"(?<=Game\s)(\d*)|(\d*)(?=\sred)|(\d*)(?=\sgreen)|(\d*)(?=\sblue)"
    p_c = re.compile(pattern=pattern)   
    l_t = [list(zip(*p_c.findall(l))) for l in lines]
    sums =[[max(map(lambda x: int(x) if x.isdigit() else 0, ttt)) for ttt in tt] for tt in l_t] 
    res = sum(list(map(lambda x: x[1]*x[2]*x[3], sums)))
    return res


if __name__=='__main__':

    TEST = False if len(sys.argv) <2 else True
    
    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        lines1 = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
        part1(lines1)
        lines2 = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]
        part2(lines2)