import copy

with open('input.txt') as f:
    starting_position = [x for x in f.read().strip().split('\n') if not x.startswith('move') and x != '']
starting_columns = []

for i in range(0, 33, 4):
    column = []
    for row in reversed(starting_position):
        position = row[i: i + 3]
        if position.startswith('[') and position.endswith(']'):
            column.append(position.strip('[').strip(']'))
    starting_columns.append(column)

with open('input.txt') as f:
    move_commands = [[int(y) for y in x.split() if y.isnumeric()]
                     for x in f.read().strip().split('\n') if x.startswith('move')]
columns = copy.deepcopy(starting_columns)

for move_command in move_commands:
    for move in range(move_command[0]):
        columns[move_command[2] - 1].append(columns[move_command[1] - 1].pop())

crate_message = ''.join([x[-1] for x in columns])
print("1:", crate_message)


columns2 = copy.deepcopy(starting_columns)

for move_command in move_commands:
    moving_crates = []
    for move in range(move_command[0]):
        moving_crates.append(columns2[move_command[1] - 1].pop())
    for i in range(len(moving_crates)):
        columns2[move_command[2] - 1].append(moving_crates.pop())

crate_message2 = ''.join([x[-1] for x in columns2])
print("2:", crate_message2)
