f = open('input2.txt')
input_list = f.read().split('\n')[:-1]

split_list = []
for row in input_list:
    row = row.split(':')
    row[0] = row[0].split(' ')
    row[0][0] = row[0][0].split('-')
    split_list.append(row)

# 1
valid_counter1 = 0
for row in split_list:
    appear_num = row[1].count(row[0][1])
    if appear_num in range(int(row[0][0][0]), int(row[0][0][1]) + 1):
        valid_counter1 += 1

print(valid_counter1)

# 2
valid_counter2 = 0
for row in split_list:
    letter_counter = 0
    if row[1][int(row[0][0][0])] == row[0][1]:
        letter_counter += 1
    if row[1][int(row[0][0][1])] == row[0][1]:
        letter_counter += 1
    if letter_counter == 1:
        valid_counter2 += 1

print(valid_counter2)



