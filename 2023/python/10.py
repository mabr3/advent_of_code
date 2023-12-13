from utils import timer, reader
import sys


class Node:
    # distance to S. if S then 0
    def __init__(self, coords, distance, type) -> None:
        self.distance = distance
        self.line = coords[0]
        self.col = coords[1]
        self.type = type
        print(self.__str__())

    def __str__(self) -> str:
        return f"I'm at ({self.line}, {self.col}), my distance is {self.distance}, my type is {self.type}"


def path(lines, node, origin):
    directions = {
        "|": ["u", "d"],
        "-": ["l", "r"],
        "F": ["d", "r"],
        "L": ["u", "r"],
        "J": ["u", "l"],
        "7": ["d", "l"],
        ".": None,
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
    if not direction:
        return node.distance
    else:
        if origin == "":
            # this is the start node, need to go through both neighbours.
            direction = directions.get(node.type)
            moves = [letter_mappings.get(d) for d in direction]
            coords = [(node.line + move[0], node.col + move[1]) for move in moves]
            types = [
                lines[coords[0][0]][coords[0][1]],
                lines[coords[1][0]][coords[1][1]],
            ]
            print(coords)
            print(types)
            return max(
                path(lines, Node(coords[0], node.distance + 1, types[0]), moves[0][2]),
                path(
                    lines,
                    Node(coords[1], node.distance + 1, types[1]),
                    moves[1][2],
                ),
            )
        else:
            print(f"{node.type}")
            print(f"{directions.get(node.type)}")

            direction = directions.get(node.type)
            direction.remove(origin)
            # Only need to go either up, down, left, or right depending on the added direction
            print(direction)
            move = letter_mappings.get(direction[0])
            print(move)
            coords = (node.line + move[0], node.col + move[1])
            neighbour = Node(coords, node.distance + 1, lines[coords[0]][coords[1]])
            return max(node.distance, path(lines, neighbour, move[2]))

    return


@timer
def part1(lines):
    # neighbord depend on shape
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
            if lines[line][col] == "S":
                s_node = Node((line, col), 0, "F")
                break

    print(s_node)
    # Go through the rest of the path a return max dist (DFS)
    RESULT = path(lines, s_node, "")
    return RESULT


@timer
def part2(lines):
    RESULT = 0
    return RESULT


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        lines1 = [".....", ".S-7.", ".|.|.", ".L-J.", "....."]
        part1(lines1)
        lines2 = ["test2"]
        part2(lines2)
