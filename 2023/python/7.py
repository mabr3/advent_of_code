from utils import timer, reader
import re
import sys
from collections import Counter
from functools import cmp_to_key

def get_type(hand):
    vals = sorted(Counter(hand).values(), reverse=True)
    if vals[0] in [4,5]:
        return vals[0]+2
    elif vals[0] == 3:
        return 5 if vals[1]  == 2 else 4
    elif vals[0] == 2:
        return 3 if vals[1] == 2 else 2
    else:
        return 1


def custom_ordering(x, y): 
    x_type, y_type = get_type(x[0]), get_type(y[0])

    dict_vals = {str(i):i for i in range(1,10)}
    dict_vals = {**dict_vals,
                 'T':10,
                 'J':11,
                 'Q':12,
                 'K':13,
                 'A':14}
    if x_type>y_type:
        return 1
    elif x_type < y_type:
        return -1
    else:
        for xx,yy in list(zip(x[0],y[0])):
            if dict_vals.get(xx)>dict_vals.get(yy):
                return 1
            elif dict_vals.get(xx)<dict_vals.get(yy):
                return -1
            else:
                pass
    return 1

def get_type_2(hand):
    nr_j = hand.count('J')
    vals = sorted(Counter(hand.replace('J','')).values(), reverse=True)
    if not vals: 
        vals, nr_j = [nr_j], 0

    if (t := vals[0] + nr_j) in [4,5]:
        return t+2
    elif (t := vals[0] + nr_j) == 3:
        return 5 if vals[1]  == 2 else 4
    elif (t := vals[0] + nr_j) == 2:
        return 3 if vals[1] == 2 else 2
    else:
        return 1


def custom_ordering_2(x, y): 
    x_type, y_type = get_type_2(x[0]), get_type_2(y[0])
    dict_vals = {str(i):i for i in range(1,10)}
    dict_vals = {**dict_vals,
                 'T':10,
                 'J':0,
                 'Q':12,
                 'K':13,
                 'A':14}
    if x_type>y_type:
        return 1
    elif x_type < y_type:
        return -1
    else:
        for xx,yy in list(zip(x[0],y[0])):
            if dict_vals.get(xx)>dict_vals.get(yy):
                return 1
            elif dict_vals.get(xx)<dict_vals.get(yy):
                return -1
            else:
                pass
    return 1

@timer
def part1(lines):
    pattern = r'(\w+)\s(\w+)'
    p_c = re.compile(pattern)
    hands = [re.match(p_c, line).groups() for line in lines]
    sorted_hands = sorted(hands, key=cmp_to_key(custom_ordering))
    RESULT = sum([int(sorted_hands[i][1])*(i+1) for i in range(len(sorted_hands))])
    return RESULT

@timer
def part2(lines):
    pattern = r'(\w+)\s(\w+)'
    p_c = re.compile(pattern)
    hands = [re.match(p_c, line).groups() for line in lines]
    sorted_hands = sorted(hands, key=cmp_to_key(custom_ordering_2))
    RESULT = sum([int(sorted_hands[i][1])*(i+1) for i in range(len(sorted_hands))])
    return RESULT


if __name__=='__main__':
    TEST = False if len(sys.argv) <2 else True
    
    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        lines1 = ['32T3K 765',
                  'T55J5 684',
                  'KK677 28',
                  'KTJJT 220',
                  'QQQJA 483']
        part1(lines1)
        lines2 = lines1
        part2(lines2)