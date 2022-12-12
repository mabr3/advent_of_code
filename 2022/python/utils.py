import fileinput
import os
import re


def get_two_parts(year, day):
    file_input = ''.join(
        fileinput.input(
            '/'.join(
                os.getcwd().split('/')[:-2]) + f'/{year}/inputs/{day}.txt'))
    p1, p2 = file_input.split('\n\n')
    return p1, p2


def parse_nums(line):
    return [int(i) for i in re.findall(r'(\d+)', line)]
