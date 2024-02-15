import itertools as it

f = open('input9.txt')
input_list = f.read().splitlines()
input_list = [int(x) for x in input_list]

# 1
for sum_index in range(25, len(input_list)):
    is_sum = False
    for index1, index2 in it.combinations(range(sum_index - 25, sum_index), 2):
        if input_list[index1] + input_list[index2] == input_list[sum_index]:
            is_sum = True
    if not is_sum:
        ans1 = input_list[sum_index]

print(ans1)

# 2
for index in range(len(input_list)):
    number_sum = 0
    i = 0
    used_list = []
    while number_sum < ans1:
        if input_list[index + i] != ans1:
            number_sum += input_list[index + i]
            used_list.append(input_list[index + i])
        if number_sum == ans1:
            used_list = sorted(used_list)
            ans2 = used_list[0] + used_list[-1]
        i += 1

print(ans2)
