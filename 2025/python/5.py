from utils import timer, reader
import sys

# TODO: do it with binary search


def check_in_range(value, ranges):
    for r in ranges:
        if value < r[0]:
            return 0
        if value >= r[0] and value <= r[1]:
            return 1
    return 0


def add_to_ranges(
    r: tuple[int, int], ranges: list[tuple[int, int]]
) -> list[tuple[int, int]]:
    if ranges == []:
        ranges.append(r)
    else:
        for i in range(len(ranges)):
            if r[1] < ranges[i][0]:
                # end of new is smaller than start of existing
                ranges = ranges[:i] + [(r)] + ranges[i:]
                return ranges
            if r[0] >= ranges[i][0] and r[1] <= ranges[i][1]:
                # already included
                return ranges
            if r[0] <= ranges[i][0] and r[1] >= ranges[i][1]:
                # new range eats the old
                ranges = ranges[:i] + add_to_ranges(r, ranges[i + 1 :])
                return ranges
            if r[0] < ranges[i][0] and r[1] >= ranges[i][0]:
                new_range = (r[0], ranges[i][1])
                ranges = ranges[:i] + add_to_ranges(new_range, ranges[i + 1 :])
                return ranges
            if r[1] > ranges[i][0] and r[0] <= ranges[i][1]:
                new_range = (ranges[i][0], r[1])
                ranges = ranges[:i] + add_to_ranges(new_range, ranges[i + 1 :])
                return ranges
        # if it reaches here then it means this ranges starts after the last end
        ranges.append(r)
    return ranges


@timer
def part1(lines):
    res = 0
    ranges = []
    for line in lines:
        entry = line.split("-")
        if len(entry) == 2:
            r = (int(entry[0]), int(entry[1]))
            ranges = add_to_ranges(r, ranges)
        elif entry[0] != "":
            res += check_in_range(int(entry[0]), ranges)
    return res


@timer
def part2(lines):
    res = 0
    ranges = []
    for line in lines:
        entry = line.split("-")
        if len(entry) == 2:
            r = (int(entry[0]), int(entry[1]))
            ranges = add_to_ranges(r, ranges)
        elif entry[0] == "":
            break

    res = sum(r[1] - r[0] + 1 for r in ranges)
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = ["3-5", "10-14", "16-20", "12-18", "", "1", "5", "8", "11", "17", "32"]
        assert part1(lines1) == 3, "should be 3"
        lines2 = lines1
        assert part2(lines2) == 14, "should be 14"
