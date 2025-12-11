import torch

inp = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

with open("day4.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")
for i, line in enumerate(inp):
    inp[i] = [1 if cell == "@" else 0 for cell in line]

inp = torch.tensor(inp).to(int)
total = 0

for i in range(len(inp)):
    i_lo = max(0, i-1)
    i_hi = min(i+2, len(inp))
    for j in range(len(inp[0])):
        j_lo = max(0, j-1)
        j_hi = min(j+2, len(inp[0]))
        if inp[i, j] == 1:
            s = (inp[i_lo:i_hi, j_lo:j_hi].sum() - inp[i, j] < 4).int().item()
            # print(i, j, i_lo, i_hi, j_lo, j_hi, inp[i_lo:i_hi, j_lo:j_hi].sum())
            total += s
    # print()

print("PART 1:", total)


# PART 2
import torch

inp = """\
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
"""

with open("day4.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")
for i, line in enumerate(inp):
    inp[i] = [1 if cell == "@" else 0 for cell in line]

inp = torch.tensor(inp).to(int)
total = 0
old = -1

while old != total:
    old = total
    for i in range(len(inp)):
        i_lo = max(0, i-1)
        i_hi = min(i+2, len(inp))
        for j in range(len(inp[0])):
            j_lo = max(0, j-1)
            j_hi = min(j+2, len(inp[0]))
            if inp[i, j] == 1:
                s = (inp[i_lo:i_hi, j_lo:j_hi].sum() - inp[i, j] < 4).int().item()
                # print(i, j, i_lo, i_hi, j_lo, j_hi, inp[i_lo:i_hi, j_lo:j_hi].sum())
                if s == 1:
                    inp[i, j] = 0
                total += s
        # print()

print("PART 2:", total)