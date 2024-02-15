with open('input.txt') as f:
    rucksacks = [[set(x[:len(x)//2]), set(x[len(x)//2:])] for x in f.read().strip().split("\n")]
print(rucksacks)
misplaced_item_types = []

for rucksack in rucksacks:
    for item in rucksack[0]:
        if item in rucksack[1]:
            misplaced_item_types.append(item)

misplaced_items_type_prio = [1 + ord(x) - ord("a") if x.islower() else 27 + ord(x) - ord("A") for x in misplaced_item_types]
print("1:", sum(misplaced_items_type_prio))


with open('input.txt') as f:
    rucksacks2 = [set(x) for x in f.read().strip().split("\n")]
elf_group_size = 3
badges = []

for i, rucksack in enumerate(rucksacks2):
    if i % elf_group_size == 0:
        for item in rucksack:
            is_badge = True
            for j in range(1, elf_group_size):
                if item not in rucksacks2[i+j]:
                    is_badge = False
            if is_badge:
                badges.append(item)

badges_type_prio = [1 + ord(x) - ord("a") if x.islower() else 27 + ord(x) - ord("A") for x in badges]
print("2:", sum(badges_type_prio))
