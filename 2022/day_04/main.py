with open('input.txt') as f:
    section_assignments = [[x.split("-") for x in x.split(",")] for x in f.read().strip().split("\n")]
print(section_assignments)
fully_contained_ranges = 0

for section_assignment in section_assignments:
    a_min, a_max = [int(x) for x in section_assignment[0]]
    b_min, b_max = [int(x) for x in section_assignment[1]]
    if a_min <= b_min and a_max >= b_max or b_min <= a_min and b_max >= a_max:
        fully_contained_ranges += 1

print("1:", fully_contained_ranges)


overlapping_pairs = 0

for section_assignment in section_assignments:
    a_min, a_max = [int(x) for x in section_assignment[0]]
    b_min, b_max = [int(x) for x in section_assignment[1]]
    if a_min in range(b_min, b_max + 1) or b_min in range(a_min, a_max + 1):
        overlapping_pairs += 1

print("2:", overlapping_pairs)

