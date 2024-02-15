with open('input.txt') as f:
    trees = [[int(y) for y in x] for x in f.read().strip().split("\n")]
visible_trees = []

for i in range(len(trees)):
    visible_trees.append([])
    for j in range(len(trees[0])):
        visible_trees[i].append(0)

for i in range(len(trees)):
    for j in range(len(trees[0])):
        if i == 0 or i == len(trees) - 1 or j == 0 or j == len(trees[0]) - 1:
            visible_trees[i][j] = 1
            continue
        if max(trees[i][:j]) < trees[i][j] or max(trees[i][j + 1:]) < trees[i][j]:
            visible_trees[i][j] = 1

        max_above = -1
        for m in range(i):
            if trees[m][j] > max_above:
                max_above = trees[m][j]

        max_under = -1
        for n in range(i + 1, len(trees)):
            if trees[n][j] > max_under:
                max_under = trees[n][j]

        if trees[i][j] > max_above or trees[i][j] > max_under:
            visible_trees[i][j] = 1

tree_counter = 0
for row in visible_trees:
    print(row)
    for visible in row:
        tree_counter += visible

print("1:", tree_counter)
