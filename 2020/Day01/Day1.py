import itertools as it
f = open('input1.txt')
input_list = list(map(int, f.read().split('\n')[:-1]))

# 1
int_set = set()
for num in input_list:
    if 2020 - num in int_set:
        print(num * (2020 - num))
        break
    int_set.add(num)

# 2
int_set = set()
for num1, num2 in it.combinations(input_list, 2):  # O(n^2)
    if 2020 - num1 - num2 in int_set:  # O(1)
        print(num1 * num2 * (2020 - num1 - num2))
        break
    int_set.add(num1)
    int_set.add(num2)



