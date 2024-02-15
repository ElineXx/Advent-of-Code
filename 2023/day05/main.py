def find_seeds_min_location(seeds, lines):
    min_location = None
    already_changed = False
    for seed in seeds:
        current_num = seed
        for line in lines:
            if line == "":
                already_changed = False
            elif line[0].isdigit() and not already_changed:
                end_num, start_num, range_num = map(int, line.split())
                if start_num <= current_num < start_num + range_num:
                    current_num = end_num + (current_num - start_num)
                    already_changed = True
        if not min_location or min_location > current_num:
            min_location = current_num

    return min_location


with open('input.txt') as f:
    lines = [x for x in f.read().strip().split("\n")]
seeds = list(map(int, lines[0].split()[1:]))

# total_min_location = None
# for i, seed in enumerate(seeds):
#
#     if i % 2 == 0:
#         min_location = find_seeds_min_location(range(seed, seeds[i + 1] + 1), lines)
#         if not total_min_location or total_min_location > min_location:
#             total_min_location = min_location

print(seeds)
print("1:", find_seeds_min_location(seeds, lines))
# print("2:", total_min_location)


with open("input.txt") as fin:
    lines = fin.read().strip().split("\n")

raw_seeds = list(map(int, lines[0].split(" ")[1:]))
seeds = [
    (raw_seeds[i], raw_seeds[i+1])
    for i in range(0, len(raw_seeds), 2)
]

# Generate all the mappings
maps = []

i = 2
while i < len(lines):
    catA, _, catB = lines[i].split(" ")[0].split("-")
    maps.append([])

    i += 1
    while i < len(lines) and not lines[i] == "":
        dstStart, srcStart, rangeLen = map(int, lines[i].split())
        maps[-1].append((dstStart, srcStart, rangeLen))
        i += 1

    maps[-1].sort(key=lambda x: x[1])

    i += 1


# Ensure that all mappings are disjoint
for m in maps:
    for i in range(len(m)-1):
        if not m[i][1] + m[i][2] <= m[i+1][1]:
            print(m[i], m[i+1])


def remap(lo, hi, m):
    # Remap an interval (lo,hi) to a set of intervals m
    ans = []
    for dst, src, R in m:
        end = src + R - 1
        D = dst - src  # How much is this range shifted

        if not (end < lo or src > hi):
            ans.append((max(src, lo), min(end, hi), D))

    for i, interval in enumerate(ans):
        l, r, D = interval
        yield (l + D, r + D)

        if i < len(ans) - 1 and ans[i+1][0] > r + 1:
            yield (r + 1, ans[i+1][0] - 1)

    # End and start ranges can use some love
    if len(ans) == 0:
        yield (lo, hi)
        return

    if ans[0][0] != lo:
        yield (lo, ans[0][0] - 1)
    if ans[-1][1] != hi:
        yield (ans[-1][1] + 1, hi)


locs = []

ans = 1 << 60

for start, R in seeds:
    cur_intervals = [(start, start + R - 1)]
    new_intervals = []

    for m in maps:
        for lo, hi in cur_intervals:
            for new_interval in remap(lo, hi, m):
                new_intervals.append(new_interval)

        cur_intervals, new_intervals = new_intervals, []

    for lo, hi in cur_intervals:
        ans = min(ans, lo)


print(ans)