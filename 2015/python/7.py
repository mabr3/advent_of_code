from utils import timer, reader
from dataclasses import dataclass
import sys
import re


@dataclass
class Wire:
    op: str
    source: tuple
    value: int = None 

    def get_value(self, wires):
        if not self.value:
            self.do_op(wires)
        return self.value

    def do_op(self, wires: dict):
        s0 = wires.get(self.source[0]).get_value(wires) if self.source[0] in wires else int(self.source[0])
        source = (s0, None) if not self.source[1] else \
            (s0, wires.get(self.source[1]).get_value(wires) if self.source[1] in wires else int(self.source[1]))

        if not self.op:
            self.value = source[0]
        elif self.op == 'NOT':
            self.value = source[0] ^ 0xFFFF
        elif self.op == 'AND':
            self.value = source[0] & source[1]
        elif self.op == 'OR':
            self.value = source[0] | source[1]
        elif self.op == 'LSHIFT':
            self.value =source[0] << source[1] 
        elif self.op == 'RSHIFT':
            self.value = source[0] >> source[1]

def print_vals(wires):
    for k in sorted(wires):
        print(f"{k}: \t{wires[k].value} ")

@timer
def part1(lines):
    wires = {}
    p1 = re.compile(
            r'^(?:(?P<val>\w+)|'
            r'(?P<left>\w+)\s(?P<op>\w+)\s(?P<right>\w+)|'
            r'NOT\s(?P<not>\w+))'
            r'\s->\s(?P<target>\w+)$'
            )

    for line in lines:
        m = re.match(p1, line).groupdict()
        if m['val']:
            source = (m['val'], None)
        elif m['not']:
            m['op'] = 'NOT'
            source = (m['not'], None)
        else:
            source = (m['left'], m['right'])
        wire = Wire(
                m.get('op'),
                source
                )
        wires[m.get('target')] = wire

    RESULT = wires.get('a', 0).get_value(wires)
    return RESULT


@timer
def part2(lines):
    wires = {}
    p1 = re.compile(
            r'^(?:(?P<val>\w+)|'
            r'(?P<left>\w+)\s(?P<op>\w+)\s(?P<right>\w+)|'
            r'NOT\s(?P<not>\w+))'
            r'\s->\s(?P<target>\w+)$'
            )

    for line in lines:
        m = re.match(p1, line).groupdict()
        if m['val']:
            source = (m['val'], None)
        elif m['not']:
            m['op'] = 'NOT'
            source = (m['not'], None)
        else:
            source = (m['left'], m['right'])
        wire = Wire(
                m.get('op'),
                source
                )
        wires[m.get('target')] = wire

    b = wires.get('a', 0).get_value(wires)
    for wire in wires:
         wires[wire].value = None
    wires['b'].value = b

    RESULT = wires.get('a', 0).get_value(wires)
    return RESULT


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = [
                '123 -> x',
                '456 -> y',
                'x AND y -> d',
                'x OR y -> e',
                'x LSHIFT 2 -> f',
                'y RSHIFT 2 -> g',
                'NOT x -> h',
                'NOT y -> i']
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
