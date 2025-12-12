# sample input
inp = """\
0:
###
##.
##.

1:
###
##.
.##

2:
.##
###
##.

3:
##.
###
##.

4:
###
#..
###

5:
###
.#.
###

4x4: 0 0 0 0 2 0
12x5: 1 0 1 0 2 2
12x5: 1 0 1 0 3 2
"""

# real input
with open("day12.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n\n")
boxes = []
for i, box in enumerate(inp[:-1]):
    box_size = box.count("#")
    box = box.split("\n")[1:]
    boxes.append((i, (box, box_size)))

boxes = dict(boxes)

total = 0
unsorted = 0
unsolveable = 0
problems = inp[-1].split("\n")
for line in problems:
    grid, present_dist = line.split(": ")
    grid = list(map(int, grid.split("x")))
    present_dist = list(map(int, present_dist.split(" ")))
    trivial_fit = grid[0] // 3 * grid[1] // 3
    num_presents = sum(present_dist)
    total_area = grid[0] * grid[1]
    presents_area = 0
    for i, N_presents in enumerate(present_dist):
        presents_area += boxes[i][1] * N_presents

    # can we stack the presents in a grid as 3x3 boxes? (trivially solveable)
    if num_presents <= trivial_fit:
        total += 1
        continue
    # do the presents cover more area than is in the grid? (trivially unsolveable)
    elif presents_area > total_area:
        unsolveable += 1
    # remaining: enough area, but would require more optimal solution
    else:
        unsorted += 1

# answer is "solveable"
print("Solveable:", total, "Unsorted:", unsorted, "Unsolveable:", unsolveable)