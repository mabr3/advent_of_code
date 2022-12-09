import os
with open('/'.join(os.getcwd().split('/')[:-1]) + "/inputs/2.txt", 'r') as f:
    lines = f.readlines()

# PART I
max_sum = 0
adder = 0
quantities = []
for line in lines:
    if line == '\n':
        quantities.append(adder)
        adder = 0
    else:
        adder += int(line.strip('\n'))

quantities.sort(reverse=True)
print(f'Solution for part I is: {quantities[0]}')

# Part II

print(f'Solution for part II is: {sum(quantities[:3])}')


