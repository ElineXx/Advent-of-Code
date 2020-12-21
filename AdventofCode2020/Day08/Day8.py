f = open('input8.txt')
input_list = f.read().splitlines()
split_list = [x.split(' ') for x in input_list]
for x in split_list:
    x[1] = x[1].strip('+')

# 1
i = 0
accumulator1 = 0
visited_indexes1 = []
while i not in visited_indexes1:
    visited_indexes1.append(i)
    move = 1
    if split_list[i][0] == 'acc':
        accumulator1 += int(split_list[i][1])
    if split_list[i][0] == 'jmp':
        move = int(split_list[i][1])
    i += move

print(accumulator1)

# 2
for j in range(len(split_list)):
    if split_list[j][0] == 'jmp':
        split_list[j][0] = 'nop'
    elif split_list[j][0] == 'nop':
        split_list[j][0] = 'jmp'

    i2 = 0
    accumulator2 = 0
    visited_indexes2 = []
    while i2 not in visited_indexes2:
        visited_indexes2.append(i2)
        move = 1
        if split_list[i2][0] == 'acc':
            accumulator2 += int(split_list[i2][1])
        if split_list[i2][0] == 'jmp':
            move = int(split_list[i2][1])
        i2 += move
        if i2 == len(split_list) - 1:
            print(accumulator2)
        if i2 >= len(split_list):
            break

    if split_list[j][0] == 'jmp':
        split_list[j][0] = 'nop'
    elif split_list[j][0] == 'nop':
        split_list[j][0] = 'jmp'
