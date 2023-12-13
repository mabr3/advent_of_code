import os

with open("/".join(os.getcwd().split("/")[:-1]) + "/inputs/3.txt", "r") as f:
    lines = f.readlines()

# PART I
adder = 0
for line in lines:
    line1, line2 = line[: int(len(line) / 2)], line[int(len(line) / 2) :]
    c = "".join(set(line1).intersection(line2))
    to_add = ord(c) % ord("a") + 1 if c > "a" else (ord(c) % ord("A") + 27)
    adder += to_add
print(f"Solution for part I is: {adder}")

# Part II
adder = 0
for r in range(0, len(lines), 3):
    c = "".join(
        set(lines[r]).intersection(set(lines[r + 1])).intersection(set(lines[r + 2]))
    ).strip("\n")
    to_add = ord(c) % ord("a") + 1 if c > "a" else (ord(c) % ord("A") + 27)
    adder += to_add
print(f"Solution for part II is: {adder}")
