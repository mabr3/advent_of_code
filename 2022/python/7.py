from utils import get_lines
import re

lines = get_lines(2022, 7)
dir_sizes = []

class FILE:
    def __init__(self, name, size=0):
        self.name = name
        self.size = size
        self.parent_dir = None
        self.children = []

    def __str__(self):
        if self.parent_dir:
            s = f'node {self.name}, parent {self.parent_dir.name}, size {self.size}, children: {[i.name for i in self.children]}'
        else:
            s = f'node {self.name},  parent is None, size {self.size}, children: {[i.name for i in self.children]}'
        return s


ROOT = None

for line in lines:
    if line[0] == '$':
        line_split = line.strip('\n').split(' ')
        cmd = line_split[1]
        if cmd == 'cd':
            target_dir = line_split[2]
            if not ROOT:
                ROOT = FILE(target_dir)
                curr = ROOT
            elif target_dir == '..':
                # go up
                curr = curr.parent_dir
            else:
                file = FILE(target_dir)
                file.parent_dir = curr
                curr.children.append(file)
                curr = file
        # ignore ls commands
    else:
        # info regarding files and dirs
        info_1, info_2 = line.split(' ')
        if info_1 == 'dir':
            pass
        else:
            file = FILE(info_2, int(info_1))
            file.parent_dir = curr
            curr.children.append(file)


sizes = {}


def dfs(node):
    # print(node)
    if not node.children:
        return node.size
    else:
        total = 0
        for child in node.children:
            # print(f"child: {child}")
            total += dfs(child)
    sizes[node] = total
    return total


used = dfs(ROOT)
# print(sizes)
AVAIL = 70000000
NEED = 30000000
MOST = sizes[ROOT]
print(f'Solution for part 1 is: {sum(i for i in sizes.values() if i < 100000)}')
print(f'Solution for part 2 is: {min(i for i in sizes.values() if AVAIL - (MOST-i) > NEED)}')


