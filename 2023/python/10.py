from utils import timer, reader
import sys
from functools import cmp_to_key
from math import sqrt, atan2, pi



class Node:
    # distance to S. if S then 0
    def __init__(self, coords, distance, type) -> None:
        self.distance = distance
        self.line = coords[0]
        self.col = coords[1]
        self.type = type

    def __str__(self) -> str:
        return f"I'm at ({self.line}, {self.col}), my distance is {self.distance}, my type is {self.type}"


def get_neighbours(lines, matrix, node):
    directions = {
        "|": ["u", "d"],
        "-": ["l", "r"],
        "F": ["d", "r"],
        "L": ["u", "r"],
        "J": ["u", "l"],
        "7": ["d", "l"],
        ".": [],
    }
    letter_mappings = {
        # each letter mapping has the offset for line, offset for col, and the origin
        # e.g. if we have to go up then we add -1 to line index, 0 to cols and we came from 'd'
        "u": (-1, 0, "d"),
        "d": (1, 0, "u"),
        "l": (0, -1, "r"),
        "r": (0, 1, "l"),
    }
    direction = directions.get(node.type)
    nodes = []
    for dir in direction:
        offset = letter_mappings.get(dir)
        new_cords = (node.line + offset[0], node.col + offset[1])
        if matrix[new_cords[0]][new_cords[1]] == 0:
            nodes.append(
                Node(new_cords, node.distance + 1, lines[new_cords[0]][new_cords[1]])
            )

    matrix[node.line][node.col] = 1 if matrix[node.line][node.col] != '.' else 2

    return nodes


def get_initial_pipe(lines, coords):
    directions_mappings = {
        ("d", "u"): "|",
        ("l", "r"): "-",
        ("d", "r"): "F",
        ("r", "u"): "L",
        ("l", "u"): "J",
        ("d", "l"): "7",
    }
    directions = {
        "|": ["d", "u"],
        "-": ["l", "r"],
        "F": ["d", "r"],
        "L": ["r", "u"],
        "J": ["l", "u"],
        "7": ["d", "l"],
        ".": [],
    }
    left = directions.get(lines[coords[0]][coords[1] - 1]) if coords[1] != 0 else None
    right = (
        directions.get(lines[coords[0]][coords[1] + 1])
        if coords[1] != len(lines[0])
        else None
    )
    up = directions.get(lines[coords[0] - 1][coords[1]]) if coords[0] != 0 else None
    down = (
        directions.get(lines[coords[0] + 1][coords[1]])
        if coords[0] != len(lines)
        else None
    )
    s_directions = []
    if left and "r" in left:
        s_directions.append("l")
    if down and "u" in down:
        s_directions.append("d")
    if right and "l" in right:
        s_directions.append("r")
    if up and "d" in up:
        s_directions.append("u")
    return directions_mappings.get(tuple(sorted(s_directions)))


def order_vertices(vertices: list)->list:
    print(vertices)
    mean_coords = (int(sum(i[0] for i in vertices)/len(vertices)), 
                  int(sum(i[1] for i in vertices)/len(vertices)))    
    print(mean_coords)
    vertices = [(v[0] - mean_coords[0],v[1] - mean_coords[1]) for v in vertices]

    def get_angle(x):
        angle = atan2(x[1],x[0])
        if angle <= 0:
            angle = 2 * pi + angle
        return angle

    def get_distance(x):
        return sqrt(x[0]*x[0] + x[1]*x[1])

    def sorting_func(x, y):
        angle_x, angle_y = get_angle(x), get_angle(y)
        if angle_x > angle_y:
            return  1
        elif angle_x < angle_y:
            return -1
        else:
            # since the centre point should b 0, no need to add it here in the calculus for euclidean dist
            return 1 if get_distance(x) <= get_distance(y) else -1
    
    vertices = sorted(vertices, key=cmp_to_key(sorting_func))
    vertices = [(v[0] + mean_coords[0],v[1] + mean_coords[1]) for v in vertices]
    print(vertices)
    return vertices


@timer
def part1(lines):
    lines = [list(line) for line in lines]
    nodes = []
    matrix = [[0] * len(lines[0]) for i in range(len(lines))]
    for line in range(len(lines)):
        for col in range(len(lines[line])):
            if lines[line][col] == "S":
                s_node = Node((line, col), 0, get_initial_pipe(lines, (line, col)))
                nodes.append(s_node)
                break
    distance_tracker = 0
    while nodes:
        node = nodes.pop(0)
        new_nodes = get_neighbours(lines, matrix, node)
        if new_nodes:
            distance_tracker = max(distance_tracker, *[i.distance for i in new_nodes])
            nodes.extend(new_nodes)

    return distance_tracker


@timer
def part2(lines):
    lines = [list(line) for line in lines]
    nodes = set()
    matrix = [[0] * len(lines[0]) for i in range(len(lines))]
    for line in range(len(lines)):
        for col in range(len(lines[line])):
            if lines[line][col] == "S":
                s_node = Node((line, col), 0, get_initial_pipe(lines, (line, col)))
                nodes.add(s_node)
                break
    vertices = set()
    while nodes:
        node = nodes.pop()
        vertices.add((node.line, node.col))
        new_nodes = get_neighbours(lines, matrix, node)
        if new_nodes:
            nodes.update(new_nodes)

    # Having the vertices, calculate the are useing the shoelace formula
    # This has to be done either counter-clockwise or clockwise and then abs()

    #vertices = order_vertices(vertices)
    # Shoelace formula
     # A = 1/2 * sum(xi * yi+1 - yi * xi+1)
    mean_coords = (int(sum(i[0] for i in vertices)/len(vertices)), 
                  int(sum(i[1] for i in vertices)/len(vertices)))    
    vertices = rotational_sort(list(vertices), mean_coords, False)
    
    area = 0.5 * sum([vertices[i][0]*vertices[i+1][1]*1.0 - 1.0*vertices[i+1][0]*vertices[i][1] for i in range(len(vertices)-1)],
                     vertices[-1][0]*vertices[0][1] - vertices[0][0]*vertices[-1][1])
    print(f"AREA -> {area}")
    # Pick's theorem
    # A = i + points/2 - 1    i - interior points
    # i = A - points/2 + 1
    result = area - len(vertices)/2.0 + 1.0
    return round(result)

from math import atan2

def argsort(seq):
    #http://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python/3382369#3382369
    #by unutbu
    #https://stackoverflow.com/questions/3382352/equivalent-of-numpy-argsort-in-basic-python 
    # from Boris Gorelik
    return sorted(range(len(seq)), key=seq.__getitem__)

def rotational_sort(list_of_xy_coords, centre_of_rotation_xy_coord, clockwise=True):
    cx,cy=centre_of_rotation_xy_coord
    angles = [atan2(x-cx, y-cy) for x,y in list_of_xy_coords]
    indices = argsort(angles)
    if clockwise:
        return [list_of_xy_coords[i] for i in indices]
    else:
        return [list_of_xy_coords[i] for i in indices[::-1]]

if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        lines1 = [".....", ".S-7.", ".|.|.", ".L-J.", "....."]
        part1(lines1)
        lines1_2 = ["..F7.", ".FJ|.", "SJ.L7", "|F--J", "LJ..."]
        part1(lines1_2) 
        lines2 = [
            "...........",
            ".S-------7.",
            ".|F-----7|.",
            ".||.....||.",
            ".||.....||.",
            ".|L-7.F-J|.",
            ".|..|.|..|.",
            ".L--J.L--J.",
            "..........."]
        part2(lines1)
        part2(lines1_2)
        part2(lines2)
