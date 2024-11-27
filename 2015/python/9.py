from utils import timer, reader
import sys



def djikstra(G):



@timer
def part1(lines):
    RESULT = 0
    return RESULT


@timer
def part2(lines):
    RESULT = 0
    return RESULT


if __name__ == '__main__':
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split('/')[-1].rstrip('.py'))
        part1(lines)
        part2(lines)
    else:
        print('Testing!')
        lines1 = ['London to Dublin = 464',
                  'London to Belfast = 518',
                  'Dublin to Belfast = 141']
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
