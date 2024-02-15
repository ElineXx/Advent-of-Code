f = open('input3.txt')
input_list = f.read().split('\n')[:-1]

row_size = len(input_list[0])

# 1
tree_counter = 0
for index, row in enumerate(input_list):
    if row[(index * 3) % row_size] == '#':
        tree_counter += 1

print(tree_counter)

# 2
total_trees = 1
slopes = (0.5, 1, 3, 5, 7)
for slope in slopes:
    tree_counter = 0
    for index, row in enumerate(input_list):
        if (index * slope) % 1 < 0.01:
            if row[int((index * slope)) % row_size] == '#':
                tree_counter += 1
    total_trees *= tree_counter

print(total_trees)

