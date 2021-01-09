import itertools

f = open('input17.txt')
start_grid = [list(x) for x in f.read().splitlines()]

active_points = set()
for x, y in itertools.product(range(len(start_grid)), range(len(start_grid[0]))):
    if start_grid[x][y] == '#':
        active_points.add((x, y, 0))

for r in range(1, 7):
    new_active_points = set()
    for x, y, z in itertools.product(range(-r, len(start_grid) + r), range(-r, len(start_grid[0]) + r), range(-r, r + 1)):
        active_counter = 0
        for i, j, k in itertools.product(range(-1, 2), repeat=3):
            if (x + i, y + j, z + k) in active_points:
                active_counter += 1
        if active_counter == 3 or (active_counter == 4 and (x, y, z) in active_points):
            new_active_points.add((x, y, z))
    active_points = new_active_points

print('1:', len(active_points))

active_points = set()
for x, y in itertools.product(range(len(start_grid)), range(len(start_grid[0]))):
    if start_grid[x][y] == '#':
        active_points.add((x, y, 0, 0))

for r in range(1, 7):
    new_active_points = set()
    for x, y, z, w in itertools.product(
        range(-r, len(start_grid) + r), 
        range(-r, len(start_grid[0]) + r), 
        range(-r, r + 1), 
        range(-r, r + 1)
    ):
        active_counter = 0
        for i, j, k, l in itertools.product(range(-1, 2), repeat=4):
            if (x + i, y + j, z + k, w + l) in active_points:
                active_counter += 1
        if active_counter == 3 or (active_counter == 4 and (x, y, z, w) in active_points):
            new_active_points.add((x, y, z, w))
    active_points = new_active_points

print('2:', len(active_points))
