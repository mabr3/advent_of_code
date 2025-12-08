from utils import timer, reader
import sys


@timer
def part1(lines):
    res = 0
    laser = [0 for _ in range(len(lines[0]))]
    for i in range(len(lines)-1):
        for j in range(len(lines[i])):
            if i==0 and lines[i][j] == 'S':
                laser[j] = 1
            elif laser[j] == 1 and lines[i+1][j] == '^':
                res +=1
                laser[j] = 0
                if j-1 >=0:
                    laser[j-1] = 1
                if j+1 < len(laser):
                    laser[j+1] = 1
    return res

MEMO = {}

@timer
def part2(lines):
    res = 0
    laser = -1
    # get first laser position
    for i in range(len(lines[0])):
        if lines[0][i] == 'S':
            laser = i
    memo = {}
    def dfs_helper(lines, lines_idx, laser_idx, memo):
        if lines_idx >= len(lines)-1:
            return 1
        left = 0
        right = 0
        i= 0
        if lines[lines_idx][laser_idx] != '^':
            return dfs_helper(lines,lines_idx + 2, laser_idx, memo)
        else:
            if (lines_idx, laser_idx) in memo.keys():
                return memo[(lines_idx, laser_idx)]
            if laser_idx - 1 >= 0:
                left += dfs_helper(lines,lines_idx + 2, laser_idx -1, memo)
            if laser_idx +1 < len(lines[i]):
                right += dfs_helper(lines,lines_idx + 2, laser_idx +1, memo)
            memo[(lines_idx, laser_idx)] = left + right
        return left + right

    res = dfs_helper(lines, 2, laser, memo)

    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = [".......S.......",
        "...............",
        ".......^.......",
        "...............",
        "......^.^......",
        "...............",
        ".....^.^.^.....",
        "...............",
        "....^.^...^....",
        "...............",
        "...^.^...^.^...",
        "...............",
        "..^...^.....^..",
        "...............",
        ".^.^.^.^.^...^.",
        "..............."]
        assert part1(lines1) == 21, "should be 21"
        lines2 = lines1
        for i in range(12, 14, 2):
            lines2_ = lines1[:i]
            print(lines2_)
            part2(lines2_)

        assert part2(lines2) == 40, "should be 40"
