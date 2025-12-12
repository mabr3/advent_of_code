from utils import timer, reader
import sys


def calculate_area(b1, b2):
    if b1[0] == b2[0]:
        length = 0
    else:
        length = b1[0] - b2[0] if b1[0] >= b2[0] else b2[0] - b1[0]
    if b1[1] == b2[1]:
        height = 0
    else:
        height = b1[1] - b2[1] if b1[1] >= b2[1] else b2[1] - b1[1]
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


def check_valid(bricks, b1, b2):
    return False


@timer
def part2(lines):
    res = 0
    # brute force it:

    red_bricks = []
    rows = {}
    cols = {}
    # for each row get min and max either red or green
    for i in range(len(lines)):
        brick = tuple(int(j) for j in lines[i].split(","))
        red_bricks.append(brick)
        row, col = brick
        print(f" Row is {row} and col is {col}")
        if row in rows.keys():
            if col < rows[row][0]:
                rows[row] = (col, rows[row][1])
            elif col > rows[row][1]:
                rows[row] = (rows[row][0], col)
        else:
            rows[row] = (col, col)
        if col in cols.keys():
            if row < cols[col][0]:
                cols[col] = (row, cols[col][1])
            elif row > cols[col][1]:
                cols[col] = (cols[col][0], row)
        else:
            cols[col] = (row, row)
        print(f"rows: {rows}")
        print(f"cols: {cols}")

    grid = [["." for _ in range(15)] for _ in range(15)]
    print(rows)
    print(cols)
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in red_bricks:
                grid[i][j] = "#"
            elif (i in cols.keys() and cols[i][0] <= j and j <= cols[i][1]) or (
                j in rows.keys() and rows[j][0] <= i and i <= rows[j][1]
            ):
                grid[i][j] = "X"
    for r in grid:
        print(r)

    # bricks = []
    # for i in range(len(lines)):
    #     brick = tuple(int(j) for j in lines[i].split(','))
    #     bricks.append(brick)
    # for i in range(len(bricks)):
    #     for j in range(i+1,len(bricks)):
    #         if check_three(bricks, i, j):
    #             area = calculate_area(bricks[i], bricks[j])
    #             if area > res:
    #                 print(f'Got area= {area} with bricks {bricks[i]} and {bricks[j]}')
    #                 res = area
    # print(bricks)
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
