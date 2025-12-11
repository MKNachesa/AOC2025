import torch

inp = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""

with open("day3.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")

total = 0

for line in inp:
    line = torch.tensor(list(map(int, list(line))))
    first_num = torch.max(line[:-1])
    idx_first_num = torch.argmax(line[:-1])
    second_num = torch.max(line[idx_first_num+1:])
    num = int(f"{first_num}{second_num}")
    total += num

print("PART 1:", total)

# PART 2
import torch

inp = """\
987654321111111
811111111111119
234234234234278
818181911112111
"""

with open("day3.txt") as f:
    inp = f.read()

inp = inp[:-1].split("\n")

total = 0

for line in inp:
    num = ""
    line = torch.tensor(list(map(int, list(line))))
    idx_biggest_num = -1
    for i in range(-11, 1):
        if i == 0:
            i = len(line)
        biggest_num = torch.max(line[idx_biggest_num+1:i])
        idx_biggest_num = torch.argmax(line[idx_biggest_num+1:i]) + idx_biggest_num + 1
        num += str(biggest_num.item())
    num = int(num)
    # print(num)
    total += num

print("PART 2:", total)