import os
with open('/'.join(os.getcwd().split('/')[:-1]) + "/inputs/4.txt", 'r') as f:
    lines = f.readlines()

# PART I
counter = 0
counter2 = 0
for line in lines:
    xy = line.strip('\n').split(',')
    x, y = [int(val) for val in xy[0].split('-')], [int(val2) for val2 in xy[1].split('-')]
    if x[0] >= y[0] and x[1] <= y[1] or\
            y[0] >= x[0] and y[1] <= x[1]:
        counter += 1
    # PART II
    if y[0] <= x[0] <= y[1] or x[0] <= y[0] <= x[1]:
        counter2 += 1
print(f'Solution for part I is: {counter}')
print(f'Solution for part II is: {counter2}')