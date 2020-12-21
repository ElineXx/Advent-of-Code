f = open('input6.txt')
input_list = f.read().split('\n')[:-1]
group_strings = ' '.join(input_list).split('  ')

# 1
total1 = 0
for string in group_strings:
    types_of_goods1 = set()
    for char in string:
        if char != ' ':
            types_of_goods1.add(char)
    total1 += len(types_of_goods1)

print(total1)

# 2
group_list = [x.split(' ') for x in group_strings]

total2 = 0
for group in group_list:
    types_of_goods2 = group[0]
    for person in group:
        for char in types_of_goods2:
            if char not in person:
                types_of_goods2 = types_of_goods2.replace(char, '')
    total2 += len(types_of_goods2)

print(total2)

