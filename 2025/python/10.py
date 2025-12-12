from utils import timer, reader
import sys


def dfs_helper(target, current, buttons, counter):
    if target == current:
        return counter
    elif buttons == []:
        return 10000000
    else:
        current_clicked = [
            not current[i] if str(i) in buttons[0] else current[i]
            for i in range(len(current))
        ]
        clicked = dfs_helper(target, current_clicked, buttons[1:], counter + 1)
        not_clicked = dfs_helper(target, current, buttons[1:], counter)
        return min(clicked, not_clicked)


@timer
def part1(lines):
    res = 0
    for line in lines:
        splits = line.split(" ")
        target_config = [
            False if light == "." else True
            for light in splits[0][1 : len(splits[0]) - 1]
        ]
        buttons = [splits[i] for i in range(1, len(splits) - 1)]
        res += dfs_helper(
            target_config, [False for _ in range(len(target_config))], buttons, 0
        )
    return res


def dfs_helper2(target, current, buttons, counter):
    print(f"Entering dfs_helper2 with current: {current}, counter: {counter}")

    def current_changer(current, button):
        return [
            current[c] + 1 if str(c) in button else current[c]
            for c in range(len(current))
        ]

    if target == current:
        print("Found it ---")
        return counter
    res = []
    for i in range(len(buttons)):
        button = buttons[i]
        res.append(
            dfs_helper2(target, current_changer(current, button), buttons, counter + 1)
        )
        print(res)

    return min(res)


@timer
def part2(lines):
    res = 0
    for line in lines:
        splits = line.split(" ")
        target_joltage = splits[-1][1:-1].split(",")
        buttons = [splits[i] for i in range(1, len(splits) - 1)]
        print(target_joltage)
        print(buttons)
        res += dfs_helper2(
            target_joltage, [0 for _ in range(len(target_joltage))], buttons, 0
        )
        break
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        print("Testing!")
        lines1 = [
            "[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}",
            "[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}",
            "[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}]",
        ]
        assert part1(lines1) == 7, "Should be 7"
        lines2 = lines1
        assert part2(lines2) == 33, "Should be 33"
