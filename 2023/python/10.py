from utils import timer, reader
import sys


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
    nodes = []
    matrix = [[0] * len(lines[0]) for i in range(len(lines))]
    for line in range(len(lines)):
        for col in range(len(lines[line])):
            if lines[line][col] == "S":
                s_node = Node((line, col), 0, get_initial_pipe(lines, (line, col)))
                nodes.append(s_node)
                break
    
    while nodes:
        node = nodes.pop(0)
        new_nodes = get_neighbours(lines, matrix, node)
        if new_nodes:
            nodes.extend(new_nodes)

    for i in range(1, len(matrix)):
        for j in range(1, len(i)):
            if matrix[i][j] == 0:
                
    return 0


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
        lines2 = lines1
        part2(lines2)
