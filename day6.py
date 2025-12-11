import math

inp = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

with open("day6.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")

problems = [[] for _ in range(len(inp[0].split()))]
                              
for line in inp[:-1]:
    numbers = line.split()
    numbers = [int(num) for num in numbers]
    for i, num in enumerate(numbers):
        problems[i].append(num)

total = 0
operations = inp[-1].split()
for i, op in enumerate(operations):
    if op == "*":
        total += math.prod(problems[i])
    elif op == "+":
        total += sum(problems[i])

print("PART 1:", total)

# PART 2 ------------------------------------------------

import torch

inp = """\
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  
"""

with open("day6.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")

problems = [[] for _ in range(len(inp[0].split()))]
operations = inp[-1].split()

max_lens = [0 for _ in range(len(inp[0].split()))]
i = 0
j = -1
op = inp[-1][0]
while i != len(inp[0]):
    if inp[-1][i] != " ":
        max_lens[j] -= 1
        j += 1
    max_lens[j] += 1
    i += 1
max_lens[j] += 1

N_problems = len(operations)

for line in inp[:-1]:
    numbers = []
    start = 0
    end = -1
    for length in max_lens:
        start = end + 1
        end += length + 1
        num = line[start:end]
        numbers.append(num)
    
    for i, num in enumerate(numbers):
        problems[i].append(num)

N_numbers = len(problems[0])
for i, problem in enumerate(problems):
    max_len = max_lens[i]
    numbers_array = torch.zeros((N_numbers, max_len), dtype=int)
    for j, num in enumerate(problem):
        for k, digit in enumerate(num):
            if digit != " ":
                digit = int(digit)
                numbers_array[j, k] = digit
            else:
                numbers_array[j, k] = -1
    # print(numbers_array)

    problem = []
    for num in numbers_array.T.tolist():
        num = [n for n in num if n != -1]
        num = int("".join(str(n) for n in num))
        problem.append(num)
    problems[i] = problem


total = 0
for i, op in enumerate(operations):
    if op == "*":
        total += math.prod(problems[i])
    elif op == "+":
        total += sum(problems[i])

print("PART 2:", total)