from utils import timer, reader
import sys

class Node:
    # distance to S. if S then 0
    def __init__(self, line, col, distance) -> None:
        self.distance = distance
        self.coords = (line, col)
        if distance == 0:
            self.type='F'
            self.neighbours = (None, None)

    def __str__(self) -> str:
        return f"I'm at ({self.coords}), my distance is {self.distance}, my type is {self.type} and my neighbours are {self.neighbours}"
        

def path(lines, node, origin, distance):
    directions = {
        '|': ('u','d'),
        '-': ('l','r'),
        'F': ('d','r'),
        'L': ('u', 'r'),
        'J': ('u', 'l'),
        '7': ('d', 'l'),
        '.': None
    }
    letter_mappings = {
        'u': (0,-1),
        'd': (0,1),
        'l': (-1, 0),
        'r':(1,0)
    }

    if not direction:
            return  node.distance
    if origin == '':
        #this is the start node, need to go through both neighbours.
        direction = directions.get(type)
        return max(path(Node()), path( Node()))
    else:
        type = node.type
        direction = directions.get(type).remove(origin)
        elif direction == 'u':
            return node.distance + path(lines, Node(node.coords[0], node.coords[1]+1, 'd', node.distance+1))
        elif direction == 'd':
        elif direction == 'l':
        elif direction == 'r':
        # Only need to go either up, down, left, or right depending on the added direction
        
    return


@timer
def part1(lines):

    #neighbord depend on shape
    # if F then right and down
    # if - then left and right
    # if | then up and down
    # if L then up and right
    # if 7 then left and down
    # if J then left and up
    # if . -> who cares

    lines = [list(line) for line in lines]
    for line in range(len(lines)):
        for col in range(len(lines[line])):
            if lines[line][col] == 'S':
                s_node = Node(line, col, 0,)
                break
    
    print(s_node)
    # Go through the rest of the path a return max dist (DFS)
    RESULT = path(lines, s_node, 0)
    return RESULT

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
        lines1 = [
            '.....',
            '.S-7.',
            '.|.|.',
            '.L-J.',
            '.....']
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)