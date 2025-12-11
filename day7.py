import torch

inp = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

with open("day7.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")

beams = torch.zeros((len(inp), len(inp[0])), dtype=int)

beams[0, inp[0].find("S")] = 1

count = 0
for i, line in enumerate(inp[1:]):
    i += 1
    for j, symb in enumerate(line):
        if beams[i-1, j] == 1:
            if symb == "^":
                if j > 0:
                    beams[i, j-1] = 1
                if j < len(line)-1:
                    beams[i, j+1] = 1
                count += 1
            else:
                beams[i, j] = 1
    # print(beams)

print("PART 1:", count)

# PART 2 -------------------------------------------------
import torch

inp = """\
.......S.......
...............
.......^.......
...............
......^.^......
...............
.....^.^.^.....
...............
....^.^...^....
...............
...^.^...^.^...
...............
..^...^.....^..
...............
.^.^.^.^.^...^.
...............
"""

with open("day7.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")

beams = torch.zeros((len(inp), len(inp[0])), dtype=int)

beams[0, inp[0].find("S")] = 1

count = 0
for i, line in enumerate(inp[1:]):
    i += 1
    for j, symb in enumerate(line):
        beam_weight = beams[i-1, j]
        if beam_weight > 0:
            if symb == "^":
                if j > 0:
                    beams[i, j-1] += beam_weight
                if j < len(line)-1:
                    beams[i, j+1] += beam_weight
                count += 1
            else:
                beams[i, j] += beam_weight
    # print(beams)

print("PART 2:", sum(beams[-1]).item())