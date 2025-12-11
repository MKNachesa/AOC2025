import cvxpy as cp
import matplotlib.pyplot as plt
import networkx as nx
import torch

inp = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

with open("day10.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")
inp = [line.split(" ") for line in inp]
for i, line in enumerate(inp):
    new_line = []
    target = line[0]
    target = target.strip("[]")
    target = [0 if pos == "." else 1 for pos in target]
    target = torch.tensor(target, dtype=int).unsqueeze(1)
    new_line.append(target)
    buttons = torch.zeros((target.shape[0], len(line[1:-1])), dtype=int)
    for j, button in enumerate(line[1:-1]):
        button = button.strip("()")
        button = button.split(",")
        button = list(map(int, button))
        buttons[button, j] = 1
    new_line.append(buttons)
    joltage = line[-1].strip("{}")
    joltage = joltage.split(",")
    joltage = list(map(int, joltage))
    joltage = torch.tensor(joltage).unsqueeze(1)
    new_line.append(joltage)
    inp[i] = new_line

total = 0
for (target, buttons, joltage) in inp:
    m = buttons.shape[1]
    n = buttons.shape[0]
    button_selection = cp.Variable((m, 1), integer=True)
    q = cp.Variable((n, 1), integer=True)
    objective = cp.sum(button_selection)
    constraints = [
        buttons @ button_selection == q * 2 + target,
        button_selection >= 0,
        button_selection <= 1,
    ]
    problem = cp.Problem(cp.Minimize(objective), constraints)
    problem.solve() # verbose=True
    res = button_selection.value
    total += res.sum()

print(f"PART 1:", total, int(total))

# PART 2 ------------------------------------------

import cvxpy as cp
import matplotlib.pyplot as plt
import networkx as nx
import torch

inp = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

with open("day10.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")
inp = [line.split(" ") for line in inp]
for i, line in enumerate(inp):
    new_line = []
    target = line[0]
    target = target.strip("[]")
    target = [0 if pos == "." else 1 for pos in target]
    target = torch.tensor(target, dtype=int).unsqueeze(1)
    new_line.append(target)
    buttons = torch.zeros((target.shape[0], len(line[1:-1])), dtype=int)
    for j, button in enumerate(line[1:-1]):
        button = button.strip("()")
        button = button.split(",")
        button = list(map(int, button))
        buttons[button, j] = 1
    new_line.append(buttons)
    joltage = line[-1].strip("{}")
    joltage = joltage.split(",")
    joltage = list(map(int, joltage))
    joltage = torch.tensor(joltage).unsqueeze(1)
    new_line.append(joltage)
    inp[i] = new_line

total = 0
for (target, buttons, joltage) in inp:
    m = buttons.shape[1]
    n = buttons.shape[0]
    button_selection = cp.Variable((m, 1), integer=True)
    objective = cp.sum(button_selection)
    constraints = [
        buttons @ button_selection == joltage,
        button_selection >= 0
    ]
    problem = cp.Problem(cp.Minimize(objective), constraints)
    problem.solve() # verbose=True
    res = button_selection.value
    total += res.sum()

print(f"PART 2:", total, int(total))

# PART 1 ALT ---------------------------
import torch

inp = """\
[.##.] (3) (1,3) (2) (2,3) (0,2) (0,1) {3,5,4,7}
[...#.] (0,2,3,4) (2,3) (0,4) (0,1,2) (1,2,3,4) {7,5,12,7,2}
[.###.#] (0,1,2,3,4) (0,3,4) (0,1,2,4,5) (1,2) {10,11,11,5,10,5}
"""

# with open("day10.txt") as f:
#     inp = f.read()

inp = inp[:-1].split("\n")
inp = [line.split(" ") for line in inp]
for i, line in enumerate(inp):
    new_line = []
    target = line[0]
    target = target.strip("[]")
    target = [0 if pos == "." else 1 for pos in target]
    target = torch.tensor(target, dtype=int).unsqueeze(1)
    new_line.append(target)
    buttons = torch.zeros((target.shape[0], len(line[1:-1])), dtype=int)
    for j, button in enumerate(line[1:-1]):
        button = button.strip("()")
        button = button.split(",")
        button = list(map(int, button))
        buttons[button, j] = 1
    new_line.append(buttons)
    joltage = line[-1].strip("{}")
    joltage = joltage.split(",")
    joltage = list(map(int, joltage))
    joltage = torch.tensor(joltage).unsqueeze(1)
    new_line.append(joltage)
    inp[i] = new_line

total = 0
for (target, buttons, joltage) in inp:
    solutions = [{i} for i in range(buttons.shape[0])]
    print(solutions)
    break