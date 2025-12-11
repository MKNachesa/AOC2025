inp = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

with open("day5.txt") as f:
    inp = f.read()

ranges, ids = inp[:-1].split("\n\n")
ranges = ranges.split("\n")
ranges = [r.split("-") for r in ranges]
ranges = [(int(start), int(end)) for (start, end) in ranges]
ids = ids.split("\n")
ids = [int(id) for id in ids]

total = 0
for id in ids:
    for r in ranges:
        if id >= r[0] and id <= r[1]:
            total += 1
            break

print("PART 1:", total)

# PART 2
inp = """\
3-5
10-14
16-20
12-18

1
5
8
11
17
32
"""

with open("day5.txt") as f:
    inp = f.read()

ranges, ids = inp[:-1].split("\n\n")
ranges = ranges.split("\n")
ranges = [r.split("-") for r in ranges]
ranges = [(int(start), int(end)) for (start, end) in ranges]

old_len = len(ranges)
new_len = 0

# iteratively combine overlapping ranges until no new overlaps are found
while old_len != new_len:
    old_len = len(ranges)
    new_ranges = [ranges[-1]]
    ranges = ranges[:-1]

    while len(ranges) > 0:
        old_range = ranges.pop()
        added = False
        for i, new_range in enumerate(new_ranges):
            # old_range: range to be added to new_ranges
            # new_range: range that old_range is compared to
            # check if:
            #   beginning of old_range is contained in new_range or begins where new_range ends
            #   OR end of old_range is contained in new_range or ends where new_range begins
            #   old_range is bigger than new_range
            # if yes, make new_range start at min between start of new_range and old_range
            #         and max of end of new_range and old_range
            # otherwise add old_range to new_ranges list
            # interpetation: old_range and new_range don't overlap/extend each other, so are separate ranges
            if (old_range[0] >= new_range[0] and old_range[0] <= new_range[1] + 1) \
            or (old_range[1] >= new_range[0] -1 and old_range[1] <= new_range[1]) \
            or (old_range[0] <= new_range[0] and old_range[1] >= new_range[1]):
                new_ranges[i] = ((min(new_range[0], old_range[0]), max(new_range[1], old_range[1])))
                added = True
                break
        if not added:
            new_ranges.append(old_range)
    ranges = new_ranges
    new_len = len(new_ranges)


total = 0
for r in new_ranges:
    total += len(range(r[0], r[1]+1))

print("PART 2:", total)

new_ranges = sorted(new_ranges, key=lambda x: x[0])