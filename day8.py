import torch
from collections import Counter
import time

start = time.time()

inp = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

N = 10

with open("day8.txt") as f:
    inp = f.read()
    N = 1000

inp = inp[:-1].split("\n")
inp = [list(map(int, line.split(","))) for line in inp]
inp = torch.tensor(inp)

N_boxes = len(inp)

dists = torch.sum((inp - inp.unsqueeze(1)) ** 2, dim=-1, dtype=int).triu()
new_max = dists.max().item() + 1000
dists[dists == 0] = new_max

circuits = torch.arange(N_boxes)

flattened_dists = dists.flatten()
closest = flattened_dists.argsort()

i = 0
while circuits.sum():
    if i == N:
        circuit_counts = list(Counter(circuits.tolist()).items())
        break
    min_con = closest[i].item()
    box_A = min_con // N_boxes
    box_B = min_con % N_boxes
    circuit_A = circuits[box_A].item()
    circuit_B = circuits[box_B].item()
    if circuit_A < circuit_B:
        circuits[circuits==circuit_B] = circuit_A
    elif circuit_B < circuit_A:
        circuits[circuits==circuit_A] = circuit_B
    i += 1

circuit_counts = sorted(circuit_counts, key=lambda x: x[1])[::-1]

counts = torch.prod(torch.tensor([count for (circuit, count) in circuit_counts[:3]])).item()
end = time.time()

print("PART 1:", counts)
print(f"{(end-start)*1000:.2f} ms")

# PART 2 ---------------------------------------
import torch
from collections import Counter

start = time.time()

inp = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

N = 10

with open("day8.txt") as f:
    inp = f.read()
    N = 1000

inp = inp[:-1].split("\n")
inp = [list(map(int, line.split(","))) for line in inp]
inp = torch.tensor(inp)
N_boxes = len(inp)

dists = torch.sum((inp - inp.unsqueeze(1)) ** 2, dim=-1, dtype=int).triu()
new_max = dists.max().item() + 1000
dists[dists == 0] = new_max

circuits = torch.arange(N_boxes)
flattened_dists = dists.flatten()
closest = flattened_dists.argsort()

i = 0
while circuits.sum():
    min_con = closest[i].item()
    box_A = min_con // N_boxes
    box_B = min_con % N_boxes
    circuit_A = circuits[box_A].item()
    circuit_B = circuits[box_B].item()
    if circuit_A < circuit_B:
        circuits[circuits==circuit_B] = circuit_A
    elif circuit_B < circuit_A:
        circuits[circuits==circuit_A] = circuit_B
    i += 1

X_A = inp[box_A][0].item()
X_B = inp[box_B][0].item()
result = X_A * X_B
end = time.time()

print("PART 2:", result)
print(f"{(end-start)*1000:.2f} ms")

# PART 1 AND 2 ---------------------------------------
import torch
from collections import Counter
import time

start = time.time()

inp = """\
162,817,812
57,618,57
906,360,560
592,479,940
352,342,300
466,668,158
542,29,236
431,825,988
739,650,466
52,470,668
216,146,977
819,987,18
117,168,530
805,96,715
346,949,466
970,615,88
941,993,340
862,61,35
984,92,344
425,690,689
"""

N = 10

with open("day8.txt") as f:
    inp = f.read()
    N = 1000

# preprocess input
inp = inp[:-1].split("\n")
inp = [list(map(int, line.split(","))) for line in inp]
inp = torch.tensor(inp, dtype=int)

# calculate distance between each box
# only fill in upper diagonal, since distances are symmetrical
N_boxes = len(inp)
dists = torch.sum((inp - inp.unsqueeze(1)) ** 2, dim=-1, dtype=int).triu()

# set all unfilled distances to be larger than already filled
# so these edges will never be selected
new_max = dists.max().item() + 1000
dists[dists == 0] = new_max

# initialise circuit ids
# circuits that will be merged will get the same id
# arbitrarily, the lower id is chosen
circuits = torch.arange(N_boxes)

# get edge order
# each id indicates the two boxes that are closest to each other
# since the id is gotten from a flat array
# will need retrieve the ids of the two boxes again 
# using modulo and division
# i.e..: box_A = id // N_boxes (row)
#        box_B = id % N_boxes (column)
flattened_dists = dists.flatten()
closest = flattened_dists.argsort()

# calc both PART 1 and PART 2
# PART 1 is done when N comparisons have been made
# PART 2 is done when all boxes belong to the same circuit id
i = 0
while circuits.sum():
    if i == N:
        # PART 1: store current circuit configuration
        # i.e., how many boxes are associated with each circuit id
        circuit_counts = list(Counter(circuits.tolist()).items())
    # get id of next two closest boxes
    min_con = closest[i].item()
    box_A = min_con // N_boxes
    box_B = min_con % N_boxes
    # get circuit ID belonging to these two boxes
    circuit_A = circuits[box_A].item()
    circuit_B = circuits[box_B].item()
    # select the lower of the two (arbitrary) as new circuit ID
    # any box that has either of the two found circuit IDs
    # will be assigned the new circuit ID
    # this also takes care of other boxes that may be in the same circuit
    # as box_A and box_B
    if circuit_A == circuit_B:
        pass
    elif circuit_A < circuit_B:
        circuits[circuits==circuit_B] = circuit_A
    elif circuit_B < circuit_A:
        circuits[circuits==circuit_A] = circuit_B
    i += 1

# PART 1: get three longest circuits, multiply the number of boxes in them
circuit_counts = sorted(circuit_counts, key=lambda x: x[1])[::-1]
counts = torch.prod(torch.tensor([count for (circuit, count) in circuit_counts[:3]]))
print("PART 1:", counts.item())

# get X coordinates of last two connected boxes, multiply them
X_A = inp[box_A][0].item()
X_B = inp[box_B][0].item()
result = X_A * X_B
end = time.time()
print("PART 2:", result)
print(f"{(end-start)*1000:.2f} ms")