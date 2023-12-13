from utils import timer, reader
import sys


@timer
def part1(lines):
    cards = [[i.split() for i in line.split(":")[1].split(" | ")] for line in lines]
    results = [int(2 ** (len(set(c[0]).intersection(set(c[1]))) - 1)) for c in cards]
    return sum(results)


@timer
def part2(lines):
    cards = [[i.split() for i in line.split(":")[1].split(" | ")] for line in lines]
    res = 0
    card_list = [1] * len(cards)
    for i in range(len(cards)):
        matches = len(set(cards[i][0]).intersection(set(cards[i][1])))
        x = card_list[0 : i + 1]
        z = card_list[i + matches + 1 :]
        y = [card_list[k] + card_list[i] for k in range(i + 1, i + matches + 1)]
        card_list = x + y + z
    res = sum(card_list)
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines)
        part2(lines)
    else:
        lines1 = [
            "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
            "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
            "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
            "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
            "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
            "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11",
        ]
        part1(lines1)
        lines2 = lines1
        part2(lines2)
