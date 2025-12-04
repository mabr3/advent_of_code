from utils import timer, reader
import sys

#TODO: try using complex numbers
#TODO: reduce iterations
#TODO: don't recalculate adj grid

def build_grid(lines):
    n_rows = len(lines)
    n_cols = len(lines[0])
    grid = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    grid = [[line[x] for x in range(n_cols)] for line in lines]
    return grid


def print_grid(grid):
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            print(f" {grid[i][j]: <3} ", end="")
        print("\n")


def add_padding(grid, value):
    # adds left col, right col, top row, down row of
    # padding to evoid out of bbounds checks
    n_rows = len(grid)
    n_cols = len(grid[0])
    row_pad = [value] * (n_cols + 2)
    new_grid = [row_pad, *[[value, *grid[i], value] for i in range(n_rows)], row_pad]
    return new_grid


def is_valid(i, j, n_rows, n_cols):
    if i < 0 or i > n_rows - 1 or j < 0 or j > n_cols - 1:
        return False
    return True


def build_adjacency(grid):
    dirs = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    n_rows = len(grid)
    n_cols = len(grid[0])
    adj_grid = [[0 for _ in range(n_cols)] for _ in range(n_rows)]
    for i in range(0, n_rows):
        for j in range(0, n_cols):
            adj_value = 0
            # only check if it is a roll:
            if grid[i][j] != "@":
                adj_grid[i][j] = -1
                continue
            for dir_i, dir_j in dirs:
                if is_valid(i + dir_i, j + dir_j, n_rows, n_cols):
                    if grid[i + dir_i][j + dir_j] == "@":
                        adj_value += 1
            adj_grid[i][j] = adj_value
    return adj_grid


@timer
def part1(lines):
    res = 0
    grid = build_grid(lines)
    adj_grid = build_adjacency(grid)
    for i in range(0, len(adj_grid)):
        for j in range(0, len(adj_grid[i])):
            if adj_grid[i][j] >= 0 and adj_grid[i][j] < 4:
                res += 1
    return res


@timer
def part2(lines):
    res = 0
    grid = build_grid(lines)
    adj_grid = build_adjacency(grid)
    c = 0
    # re calc adj in every run.
    while True:
        to_remove = 0
        for i in range(0, len(adj_grid)):
            for j in range(0, len(adj_grid[i])):
                if adj_grid[i][j] >= 0 and adj_grid[i][j] < 4:
                    to_remove += 1
                    grid[i][j] = "."
        # print(f"On round {c}, remove {to_remove} rolls")
        # Break on a run with 0 removals
        if to_remove == 0:
            break
        c += 1
        res += to_remove
        adj_grid = build_adjacency(grid)

    return res



if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True
    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = ["..@@.@@@@.",
            "@@@.@.@.@@",
            "@@@@@.@.@@",
            "@.@@@@..@.",
            "@@.@@@@.@@",
            ".@@@@@@@.@",
            ".@.@.@.@@@",
            "@.@@@.@@@@",
            ".@@@@@@@@.",
            "@.@.@@@.@.",
        ]
        assert part1(lines1) == 13, "Should be 13"
        lines2 = lines1
        assert part2(lines2) == 43, "Should be 43"
