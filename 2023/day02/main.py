with open('input.txt') as f:
    games = [x for x in f.read().strip().split("\n")]

results = [[[z.strip() for z in y.split(",")] for y in x.split(":")[1].split(";")] for x in games]
colors = ["red", "green", "blue"]
colors_threshold = [12, 13, 14]
sum_ids = 0
sum_powers = 0

for i, result in enumerate(results, 1):
    colors_min = [0, 0, 0]

    for round in result:
        for num_cubes in round:
            number = int(num_cubes.split(" ")[0])
            for j, color in enumerate(colors):
                if num_cubes.endswith(color) and number > colors_min[j]:
                    colors_min[j] = number

    possible = True
    for k, color_min in enumerate(colors_min):
        if color_min > colors_threshold[k]:
            possible = False
    if possible:
        sum_ids += i

    power = 1
    for color_min in colors_min:
        power *= color_min
    sum_powers += power

print("1:", sum_ids)
print("2:", sum_powers)
