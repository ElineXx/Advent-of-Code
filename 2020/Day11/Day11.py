f = open('input11.txt')
input_list = f.read().splitlines()
input_grid = [list(x) for x in input_list]

g = open('klad.txt')
test_list = g.read().splitlines()
test_grid = [list(x) for x in test_list]


# 1
def grid_changer1(grid):
    new_grid = []
    for m in range(len(grid)):
        row = []
        for n in range(len(grid[0])):
            row.append('.')
        new_grid.append(row)

    for y in range(len(grid)):
        for x in range(len(grid[0])):
            occu_counter = 0
            for j in range(y - 1, y + 2):
                if j < 0 or j >= len(grid):
                    continue
                for i in range(x - 1, x + 2):
                    if i < 0 or i >= len(grid[0]):
                        continue
                    if grid[j][i] == '#':
                        occu_counter += 1
            if grid[y][x] == 'L':
                new_grid[y][x] = '#' if occu_counter == 0 else 'L'
            if grid[y][x] == '#':
                new_grid[y][x] = 'L' if occu_counter >= 5 else '#'

    return new_grid


def stable_seats(grid, func, times):
    for k in range(times):
        grid = func(grid)
    return grid


stable_grid1 = stable_seats(input_grid, grid_changer1, 100)
ans_string = ''
for s_row in stable_grid1:
    ans_string += ''.join(s_row)
ans1 = ans_string.count('#')
print(ans1)


# 2
def grid_changer2(grid):
    new_grid = []
    for m in range(len(grid)):
        row = []
        for n in range(len(grid[0])):
            row.append('.')
        new_grid.append(row)

    for y in range(len(grid)):
        for x in range(len(grid[0])):

            occu_counter = 0

            line_count = [0, 0]
            for j in range(len(grid)):
                if grid[j][x] == '#' and j < y:
                    line_count[0] = 1
                if grid[j][x] == '#' and j > y:
                    line_count[1] = 1
            occu_counter += sum(line_count)

            line_count = [0, 0]
            for i in range(len(grid[0])):
                if grid[y][i] == '#' and i < x:
                    line_count[0] = 1
                if grid[y][i] == '#' and i > x:
                    line_count[1] = 1
            occu_counter += sum(line_count)

            line_count = [0, 0, 0, 0]
            for k in range(-100, 100):
                if (0 <= y + k < len(grid) and
                        0 <= x + k < len(grid[0])):
                    if grid[y + k][x + k] == '#' and k < 0:
                        line_count[0] = 1
                    if grid[y + k][x + k] == '#' and k > 0:
                        line_count[1] = 1

                if (0 <= y + k < len(grid) and
                        0 <= x - k < len(grid[0])):
                    if grid[y + k][x - k] == '#' and k < 0:
                        line_count[2] = 1
                    if grid[y + k][x - k] == '#' and k > 0:
                        line_count[3] = 1
            occu_counter += sum(line_count)

            if grid[y][x] == 'L':
                new_grid[y][x] = '#' if occu_counter == 0 else 'L'
            if grid[y][x] == '#':
                new_grid[y][x] = 'L' if occu_counter >= 5 else '#'
    [print(x) for x in new_grid]
    print('---')
    return new_grid


stable_grid2 = stable_seats(test_grid, grid_changer2, 5)
ans_string = ''
for s_row in stable_grid2:
    ans_string += ''.join(s_row)
ans2 = ans_string.count('#')
print(ans2)
