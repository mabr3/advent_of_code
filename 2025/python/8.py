from utils import timer, reader
import sys
import math


def calc_dist(p, q):
    dist = math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2 + (p[2] - q[2]) ** 2)
    return dist


@timer
def part1(lines, connections):
    res = 0
    boxes = []
    dists = []
    for i in range(len(lines)):
        p = tuple([int(x) for x in lines[i].split(",")])
        for j in range(len(boxes)):
            dists.append((j, i))
        boxes.append(p)

    dists = sorted(dists, key=lambda x: calc_dist(boxes[x[0]], boxes[x[1]]))
    circuits = [[i] for i in range(len(boxes))]
    boxes_place = [i for i in range(len(boxes))]

    for c in range(connections):
        p, q = dists[c]
        while boxes_place[p] != p:
            p = boxes_place[p]

        while boxes_place[q] != q:
            q = boxes_place[q]
        if p == q:
            continue
        circuits[p] += circuits[q]
        circuits[q] = []
        boxes_place[q] = p
    circuits = [set(c) for c in circuits]
    circuits = sorted([len(c) for c in circuits], reverse=True)
    res = circuits[0] * circuits[1] * circuits[2]
    return res


@timer
def part2(lines):
    res = 0
    boxes = []
    dists = []
    for i in range(len(lines)):
        p = tuple([int(x) for x in lines[i].split(",")])
        for j in range(len(boxes)):
            dists.append((j, i))
        boxes.append(p)

    dists = sorted(dists, key=lambda x: calc_dist(boxes[x[0]], boxes[x[1]]))
    circuits = [[i] for i in range(len(boxes))]
    boxes_place = [i for i in range(len(boxes))]

    for c in range(len(dists)):
        p, q = dists[c]
        while boxes_place[p] != p:
            p = boxes_place[p]

        while boxes_place[q] != q:
            q = boxes_place[q]
        if p == q:
            continue
        circuits[p] += circuits[q]
        circuits[q] = []
        boxes_place[q] = p
        if len(circuits[p]) == len(boxes):
            break
    res = boxes[dists[c][0]][0] * boxes[dists[c][1]][0]
    return res


if __name__ == "__main__":
    TEST = False if len(sys.argv) < 2 else True

    if not TEST:
        lines = reader(__file__.split("/")[-1].rstrip(".py"))
        part1(lines, 1000)
        part2(lines)
    else:
        print("Testing!")
        lines1 = [
            "162,817,812",
            "57,618,57",
            "906,360,560",
            "592,479,940",
            "352,342,300",
            "466,668,158",
            "542,29,236",
            "431,825,988",
            "739,650,466",
            "52,470,668",
            "216,146,977",
            "819,987,18",
            "117,168,530",
            "805,96,715",
            "346,949,466",
            "970,615,88",
            "941,993,340",
            "862,61,35",
            "984,92,344",
            "425,690,689",
        ]
        assert part1(lines1, 10) == 40, "should be 40"
        lines2 = lines1
        assert part2(lines2) == 25272, "should be 25272"
