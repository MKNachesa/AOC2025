inp = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

with open("day2.txt") as f:
    inp = f.read()

ranges = inp.strip("\n").split(",")

total = 0

for r in ranges[:]:
    start, end = r.split("-")
    start = int(start)
    end = int(end)
    for id in range(start, end+1):
        id = str(id)
        for i in range(1, len(id)//2+1):
            tmp_id = id
            pattern = id[:i]
            tmp_id = tmp_id.replace(pattern, "", 2)
            # print(id, tmp_id, pattern)
            if tmp_id == "":
                # print("yes")
                total += int(id)
                # print(int(id))
                break
        # print()
    # break

print("PART 1:", total)

inp = """\
11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124
"""

with open("day2.txt") as f:
    inp = f.read()

ranges = inp.strip("\n").split(",")

total = 0

for r in ranges[:]:
    start, end = r.split("-")
    start = int(start)
    end = int(end)
    for id in range(start, end+1):
        id = str(id)
        for i in range(1, len(id)//2+1):
            tmp_id = id
            pattern = id[:i]
            tmp_id = tmp_id.replace(pattern, "")
            # print(id, tmp_id, pattern)
            if tmp_id == "":
                # print("yes")
                total += int(id)
                # print(int(id))
                break
        # print()
    # break

print("PART 2:", total)