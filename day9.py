import torch
from tqdm import tqdm
import matplotlib.pyplot as plt

inp = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

with open("day9.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")
inp = [list(map(int, line.split(","))) for line in inp]
inp = torch.tensor(inp, dtype=int)

rectangles = torch.prod(torch.abs(inp - inp.unsqueeze(1)) + 1, dim=-1)
largest_rect = torch.max(rectangles).item()
print("PART 1:", largest_rect)

# PART 2 ---------------------------------------------------
import torch

inp = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

with open("day9.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")
inp = [list(map(int, line.split(","))) for line in inp]
inp = torch.tensor(inp, dtype=int)

x_to_sparse = dict()
y_to_sparse = dict()
i = 1
for x in sorted(list(set(inp[:,0].tolist()))):
    x_to_sparse[x] = i
    i += 2

i = 1
for y in sorted(list(set(inp[:,1].tolist()))):
    y_to_sparse[y] = i
    i += 2

sparse_inp = torch.zeros(inp.shape, dtype=int)
for i, (x, y) in enumerate(inp.tolist()):
    sparse_inp[i] = torch.tensor([x_to_sparse[x], y_to_sparse[y]])

field = torch.zeros((torch.max(sparse_inp[:,1])+2, torch.max(sparse_inp[:,0])+3), dtype=int)
for j, i in sparse_inp:
    field[i, j] = 1

for i in range(len(sparse_inp)):
    coor_A = sparse_inp[i].tolist()[::-1]
    coor_B = sparse_inp[(i+1)%len(sparse_inp)].tolist()[::-1]
    if coor_A[0] == coor_B[0]:
        other_coors = sorted([coor_A[1], coor_B[1]])
        field[coor_A[0],other_coors[0]:other_coors[1]] = 1
    elif coor_A[1] == coor_B[1]:
        other_coors = sorted([coor_A[0], coor_B[0]])
        field[other_coors[0]:other_coors[1],coor_A[1]] = 1

coor_A = sparse_inp[0].tolist()[::-1]
old_field = field.clone()
sign = 1
for i in range(2, len(sparse_inp)-1):
    coor_B = sparse_inp[i].tolist()[::-1]
    Ys = sorted([coor_A[0], coor_B[0]])
    Xs = sorted([coor_A[1], coor_B[1]])
    Ys[0] += 1
    Xs[0] += 1
    temp_field = torch.zeros((torch.max(sparse_inp[:,1])+2, torch.max(sparse_inp[:,0])+3), dtype=int)
    temp_field[Ys[0]:Ys[1]+1, Xs[0]:Xs[1]+1] = 1
    field = field + temp_field * sign
    sign *= -1

field = (field != 0).int()
field[old_field==1] = 1

rectangles = torch.prod(torch.abs(inp - inp.unsqueeze(1)) + 1, dim=-1).triu()
largest_rects = rectangles.flatten().argsort(descending=True)
N_squares = len(sparse_inp)

for i, ID in enumerate(largest_rects):
    # fig, ax = plt.subplots()
    pos_A = ID // N_squares
    pos_B = ID % N_squares
    coor_A = sparse_inp[pos_A].tolist()
    coor_B = sparse_inp[pos_B].tolist()
    Xs = sorted([coor_A[0], coor_B[0]])
    Ys = sorted([coor_A[1], coor_B[1]])
    inner_rect = field[Ys[0]+1:Ys[1], Xs[0]+1:Xs[1]]
    # tmp_field = field.clone().to(float)
    # tmp_field[Ys[0]:Ys[1]+1, Xs[0]:Xs[1]+1] = 0.5
    # ax.imshow(tmp_field)
    # plt.show()
    # plt.close()
    if inner_rect.sum() == torch.prod(torch.tensor(inner_rect.shape)):
        break
largest_rect = rectangles[pos_A, pos_B].item()
print("PART 2:", largest_rect)

# PART 2 ALTERNATIVE (SLOWER)

import torch

inp = """\
7,1
11,1
11,7
9,7
9,5
2,5
2,3
7,3
"""

with open("day9.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")
inp = [list(map(int, line.split(","))) for line in inp]
inp = torch.tensor(inp, dtype=int)

x_to_sparse = dict()
y_to_sparse = dict()
i = 1
for x in sorted(list(set(inp[:,0].tolist()))):
    x_to_sparse[x] = i
    i += 2

i = 1
for y in sorted(list(set(inp[:,1].tolist()))):
    y_to_sparse[y] = i
    i += 2

sparse_inp = torch.zeros(inp.shape, dtype=int)
for i, (x, y) in enumerate(inp.tolist()):
    sparse_inp[i] = torch.tensor([x_to_sparse[x], y_to_sparse[y]])

field = torch.zeros((torch.max(sparse_inp[:,1])+2, torch.max(sparse_inp[:,0])+3), dtype=int)
for j, i in sparse_inp:
    field[i, j] = 1

for i in range(len(sparse_inp)):
    coor_A = sparse_inp[i].tolist()[::-1]
    coor_B = sparse_inp[(i+1)%len(sparse_inp)].tolist()[::-1]
    if coor_A[0] == coor_B[0]:
        other_coors = sorted([coor_A[1], coor_B[1]])
        field[coor_A[0],other_coors[0]:other_coors[1]] = 1
    elif coor_A[1] == coor_B[1]:
        other_coors = sorted([coor_A[0], coor_B[0]])
        field[other_coors[0]:other_coors[1],coor_A[1]] = 1

current_points = {(0, 0)}

with tqdm() as pbar:
    while len(current_points) > 0:
        # 8 directions lmao
        new_points = set()
        for cur_i, cur_j in current_points:
            field[cur_i, cur_j] = -1
            for i in [-1, 0, 1]:
                new_i = cur_i + i
                if not (new_i >= 0 and new_i < field.shape[0]):
                    continue
                for j in [-1, 0, 1]:
                    if i == j:
                        continue
                    new_j = cur_j + j
                    if not (new_j >= 0 and new_j < field.shape[1]):
                        continue
                    new_point = (new_i, new_j)
                    if field[new_i, new_j] == 0 and new_point not in current_points:
                        new_points.add(new_point)
        current_points = new_points
        pbar.set_postfix({"len": len(current_points)})
            
field[field==0] = 1
field[field==-1] = 0

rectangles = torch.prod(torch.abs(inp - inp.unsqueeze(1)) + 1, dim=-1).triu()
largest_rects = rectangles.flatten().argsort(descending=True)
N_squares = len(sparse_inp)

for i, ID in enumerate(largest_rects):
    pos_A = ID // N_squares
    pos_B = ID % N_squares
    coor_A = sparse_inp[pos_A].tolist()
    coor_B = sparse_inp[pos_B].tolist()
    Xs = sorted([coor_A[0], coor_B[0]])
    Ys = sorted([coor_A[1], coor_B[1]])
    inner_rect = field[Ys[0]+1:Ys[1], Xs[0]+1:Xs[1]]
    if inner_rect.sum() == torch.prod(torch.tensor(inner_rect.shape)):
        break
largest_rect = rectangles[pos_A, pos_B].item()
print("PART 2:", largest_rect)

