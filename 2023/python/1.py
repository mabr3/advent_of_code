from utils import timer, reader
import re
import sys

@timer
def part1(lines):
    pattern = r'\d{1}'
    p_c = re.compile(pattern=pattern)
    vals = [ int(p_c.findall(line)[0]) *10 + int(p_c.findall(line)[-1]) for line in lines]
    return sum(vals)

@timer
def part2(lines):
    numbers = {
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9
    }
    number_string = '|'.join(numbers.keys())
    pattern = fr'(?=(\d|{number_string}))'
    p_c = re.compile(pattern=pattern)
    numbers = {
            **numbers,
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9
        }
    
    vals = [ numbers.get(p_c.findall(line)[0])*10 + numbers.get(p_c.findall(line)[-1]) for line in lines]

    return sum(vals)


if __name__=='__main__':
    
    TEST = False if len(sys.argv) <2 else True
    
    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        lines1 = ["1abc2","pqr3stu8vwx","a1b2c3d4e5f","treb7uchet"]
        part1(lines1)
        lines2 = ["two1nine","eightwothree","abcone2threexyz","xtwone3four","4nineeightseven2","zoneight234","7pqrstsixteen"]
        part2(lines2)