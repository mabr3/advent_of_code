import os

with open("/".join(os.getcwd().split("/")[:-1]) + "/inputs/2.txt", "r") as f:
    lines = f.readlines()

# PART I
#
draw = 3
win = 6
loss = 0
# scores for me:
scores = {"X": 1, "Y": 2, "Z": 3, "A": 1, "B": 2, "C": 3}
points = 0
plays = []
for line in lines:
    x, y = line.strip("\n").split(" ")
    plays.append((x, y))
    game = scores[x] - scores[y]
    if game == 0:
        result = draw
    else:
        result = win if game in (-1, 2) else loss
    points += scores[y] + result
print(f"Solution for part I is: {points}")

# Part II
points = 0
for play in plays:
    if play[1] == "X":
        result = loss
        if play[0] == "A":
            value = scores["C"]
        elif play[0] == "B":
            value = scores["A"]
        else:
            value = scores["B"]
    elif play[1] == "Y":
        result = draw
        value = scores[play[0]]
    else:
        result = win
        if play[0] == "A":
            value = scores["B"]
        elif play[0] == "B":
            value = scores["C"]
        else:
            value = scores["A"]
    points += value + result
print(f"Solution for part II is: {points}")
