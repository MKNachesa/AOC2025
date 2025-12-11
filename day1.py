# problem: https://adventofcode.com/2025/day/1
# decoding a safe

import torch

# example input
inp = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

# full input
with open("day1.txt") as f:
    inp = f.read()

# preprocess input
inp = inp.split("\n")[:-1]
inp = [int(n[1:]) * -1 if n[0] == "L" else int(n[1:]) for n in inp]

# initialise a square matrix one size larger than input length
a = torch.zeros((len(inp)+1, len(inp)+1))
a[0] = 50
# fill rows in step-wise (create upper triangle)
for i in range(1, len(inp)+1):
    a[i, i:] = inp[i-1]

# sum columns. All columns that are a multiple of 100 are our solution
solution = a.sum(dim=0) % 100

print("PART 1:", (solution == 0).sum().item())

# PART 2 ------------------------------------------------------------
# example input
inp = """\
L68
L30
R48
L5
R60
L55
L1
L99
R14
L82
"""

# full input
with open("day1.txt") as f:
    inp = f.read()

# preprocess input
inp = inp.split("\n")[:-1]
inp = [int(n[1:]) * -1 if n[0] == "L" else int(n[1:]) for n in inp]

# objective: count the number of times we passed 0
# lazy solution: for each number, take each dial tick manually
# any time a dial tick lands on 0, increment 'pass_0'
num = 50
pass_0 = 0
for i in inp:
    if i < 0:
        sign = -1
    else:
        sign = 1
    for j in range(abs(i)):
        num += sign
        num = num % 100
        if num == 0:
            pass_0 += 1

print("PART 2:", pass_0)