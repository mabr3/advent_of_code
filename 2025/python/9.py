from utils import timer, reader
import sys


def calculate_area(b1, b2):
    if b1[0] == b2[0]:
        length = 0
    else:
        length = abs(b1[0] - b2[0])
    if b1[1] == b2[1]:
        height = 0
    else:
        height = abs(b1[1] - b2[1])
    return (length + 1) * (height + 1)


@timer
def part1(lines):
    res = 0
    bricks = []
    for line in lines:
        brick = tuple(int(i) for i in line.split(","))
        for b in bricks:
            area = calculate_area(b, brick)
            if area > res:
                res = area
        bricks.append(brick)
    return res


def check_intersect(x1, y1, x2, y2, bricks):
    n = len(bricks)
    for i in range(n):
        e1 = bricks[i]
        e2 = bricks[(i - 1) % n]

        if e1[0] == e2[0]:
            if x1 < e1[0] < x2:  # is not on the boundary or out
                if max(e1[1], e2[1]) > y1 and min(e1[1], e2[1]) < y2:
                    return True
        else:
            if y1 < e1[1] < y2:
                if max(e1[0], e2[0]) > x1 and min(e1[0], e2[0]) < x2:
                    return True
    return False


def is_valid(b1, b2, memo, bricks):
    x1, x2 = sorted([b1[0], b2[0]])
    y1, y2 = sorted([b1[1], b2[1]])

    # Check vertices of the square
    for x, y in [(x1, y1), (x1, y2), (x2, y1), (x2, y2)]:
        inside = True
        if (x, y) in memo:
            inside = memo.get((x, y))
        else:
            inside = point_in_polygon(x, y, bricks)
            memo[(x, y)] = inside
        if not inside:
            return False
    # if all vertices are in the polygon
    # check if any edge intercepts the rectangle. if it does it's bad news
    return not check_intersect(x1, y1, x2, y2, bricks)


def point_in_polygon(x, y, bricks):
    # starts as false because odd means inside
    inside = False
    n = len(bricks)
    # check if point is in boundaries: counts as inside
    for i in range(n):
        b1 = bricks[i]
        b2 = bricks[(i + 1) % n]
        if (x == b1[0] == b2[0] and min(b1[1], b2[1]) <= y <= max(b1[1], b2[1])) or (
            y == b1[1] == b2[1] and min(b1[0], b2[0]) <= x <= max(b1[0], b2[0])
        ):
            return True
        # intersect boundaries
        # XOR to avoid division by zero
        if b1[0] == b2[0]:
            continue
        if ((b1[0] > x) != (b2[0] > x)) and (
            y < b1[1] + (x - b1[0]) * (b2[1] - b1[1]) / (b2[0] - b1[0])
        ):
            inside = not inside

    return inside


@timer
def part2(lines):
    res = 0
    bricks = []
    memo = {}
    for line in lines:
        brick = tuple(int(i) for i in line.split(","))
        bricks.append(brick)
    # Use ray casting
    # In any shape it crosses boundaries an odd number of times
    # it is inside. If even, it is outside
    # the input always keeps last x or y
    for id1, b1 in enumerate(bricks):
        for id2, b2 in enumerate(bricks, start=1):
            area = calculate_area(b1, b2)
            if area > res and is_valid(b1, b2, memo, bricks):
                res = area
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = ["7,1", "11,1", "11,7", "9,7", "9,5", "2,5", "2,3", "7,3"]
        assert part1(lines1) == 50, "should be 50"
        lines2 = lines1
        assert part2(lines2) == 24, "should be 24"
