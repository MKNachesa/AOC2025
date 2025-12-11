import torch

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

with open("day1.txt") as f:
    inp = f.read()

inp = inp.split("\n")[:-1]
inp = [int(n[1:]) * -1 if n[0] == "L" else int(n[1:]) for n in inp]

a = torch.zeros((len(inp)+1, len(inp)+1))
a[0] = 50

for i in range(1, len(inp)+1):
    a[i, i:] = inp[i-1]

for row in a[1:]:
    a[0] += row
    a[0] = a[0] % 100

print("PART 1:", (a[0] == 0).sum().item())


# PART 2 ---
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

with open("day1.txt") as f:
    inp = f.read()

inp = inp.split("\n")[:-1]
inp = [int(n[1:]) * -1 if n[0] == "L" else int(n[1:]) for n in inp]

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