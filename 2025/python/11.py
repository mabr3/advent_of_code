from utils import timer, reader
import sys


@timer
def part1(lines):
    res = 0
    connections = {}
    for line in lines:
        splits = line.split(":")
        key = splits[0]
        values = [i for i in splits[1].split()]
        connections[key] = values

    paths = {}

    def helper(key, connections):
        if key == "out":
            return 1
        elif key in paths:
            return paths[key]
        else:
            counter = 0
            for v in connections[key]:
                counter += helper(v, connections)
            paths[key] = counter
            return counter

    res = helper("you", connections)
    return res


@timer
def part2(lines):
    res = 0
    connections = {}
    for line in lines:
        splits = line.split(":")
        key = splits[0]
        values = [i for i in splits[1].split()]
        connections[key] = values

    # final_paths = []
    # # BFS TAKES TOO LONG
    # but we can do 3 times BFS and multiply the paths I gues
    paths = {}

    def helper(key, target, connections):
        if key == target:
            return 1
        elif key in paths:
            return paths[key]
        else:
            counter = 0
            for v in connections[key]:
                counter += helper(v, target, connections)
            paths[key] = counter
            return counter

    c = []
    for src, dest in [("out", "fft"), ("fft", "dac"), ("dac", "out")]:
        paths = {}
        c.append(helper(src, dest, connections))

    print(c)
    # # BFS to find all paths
    # #initial queue are the neighbours of svr
    # queue = [['svr']]
    # while queue:
    #     path = queue[0]
    #     queue = queue[1:]
    #     current = path[-1]
    #     if current == 'out':
    #         if 'dac' in path and 'fft' in path:
    #             final_paths.append(path)
    #         continue
    #     for c in connections[current]:
    #         new_path = [p for p in path]
    #         new_path.append(c)
    #         queue.append(new_path)
    # # DFS instead
    # known_paths = {}
    # queue = []
    # def dfs(src, dst,connections, path):
    #     print(f'Entering DFS with src {src}, dst {dst}, path {path}')
    #     path.append(src)
    #     if src == dst:
    #         if 'dac' in path and 'fft' in path:
    #             print(f'appending {path}')
    #             final_paths.append(path.copy())
    #             return
    #     else:
    #         for c in connections[src]:
    #             dfs(c, dst, connections, path)
    #     path = path[:-1]
    #
    # path =[]
    # dfs('svr', 'out', connections, path)
    # # for p in final_paths:
    # #     print(p)
    # # print(final_paths)
    #
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
            "aaa: you hhh",
            "you: bbb ccc",
            "bbb: ddd eee",
            "ccc: ddd eee fff",
            "ddd: ggg",
            "eee: out",
            "fff: out",
            "ggg: out",
            "hhh: ccc fff iii",
            "iii: out",
        ]
        assert part1(lines1) == 5, "should be 5"
        lines2 = [
            "svr: aaa bbb",
            "aaa: fft",
            "fft: ccc",
            "bbb: tty",
            "tty: ccc",
            "ccc: ddd eee",
            "ddd: hub",
            "hub: fff",
            "eee: dac",
            "dac: fff",
            "fff: ggg hhh",
            "ggg: out",
            "hhh: out",
        ]
        assert part2(lines2) == 2, "should be 2"
