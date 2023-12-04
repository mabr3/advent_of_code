from utils import timer, reader
import re
import sys

@timer
def part1(lines):
    matrix = [list(l) for l in lines]
    res = 0
    len_m = len(matrix)
    len_l = len(matrix[0])
    for i in range(len_m):
        true_counter = 0
        c=0
        to_add = left = right = up = down = False
        for j in range(len_l):
            if matrix[i][j].isdigit():
                if not to_add:
                    #check neighbors
                    #left stuff and in the same col only need to be checked if c==0
                    if c==0:
                        if j-1 >=0:
                            #checks left and right
                            vals = matrix[i][max(j-1,0):min(j+1,len_l)+1]
                            to_add = any([k !='.' and not k.isalnum() for k in vals ])
                            true_counter +=1 if to_add is True else 0
                        if not to_add and i-1 >=0:
                            # Check up
                            vals = matrix[i-1][max(j-1,0):min(j+1,len_l)+1]
                            to_add = any([k !='.' and not k.isalnum() for k in vals ])
                        if not to_add and i +1 < len_m:
                            # Check down
                            vals = matrix[i+1][max(j-1,0):min(j+1,len_l)+1]
                            to_add = any([k !='.' and not k.isalnum() for k in vals ])
                    else:
                        if j + 1 < len_l:
                            # Check right
                            vals=[]
                            rr = range(max(i-1,0),min(i+1, len_m-1)+1)
                            for r in rr:
                                vals.append(matrix[r][j+1])
                            to_add = any([k !='.' and not k.isalnum() for k in vals ])
                c+=1
            if j == len_l-1 or not matrix[i][j+1].isdigit():
                if to_add:
                    #add number and reset flag/counter
                    res += int(''.join(matrix[i][j-c+1:j+1])) 
                to_add=False
                c=0
                true_counter = 0
    return res


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
        lines1=["467..114..",
                "...*......",
                "..35..633.",
                "......#...",
                "617*......",
                ".....+.58.",
                "..592.....",
                "......755.",
                "...$.*....",
                ".664.598.."]
        part1(lines1)
        lines2 = lines1
        part2(lines2)
