from math import comb

f = open('input10.txt')
input_list = f.read().splitlines()
input_list = sorted([int(x) for x in input_list])
input_list.insert(0, 0)
input_list.append(input_list[-1] + 3)

# 1
i = 1
diff_counter = [0, 0, 0, 0]
while i < len(input_list):
    x = input_list[i] - input_list[i - 1]
    diff_counter[x] += 1
    i += 1

print(diff_counter[1] * diff_counter[3])

# 2
i = 1
total_arr = 1
while i < len(input_list) - 1:
    arr_list = []
    while input_list[i + 1] - input_list[i] == 1 and input_list[i] - input_list[i - 1] == 1:
        arr_list.append(input_list[i])
        i += 1
    possible_arr = 0
    for num in range(len(arr_list)):
        possible_arr += comb(len(arr_list), num)
    if len(arr_list) <= 2:
        possible_arr += 1
    total_arr *= possible_arr
    i += 1

print(total_arr)


# test = [0, 1, 2, 3] 0 en 3 vaste plek
# [1, 2, (1,2)]
# totaal: 1 + 2 + 1
# test = [0, 1, 2, 3, 4] 0 en 4 vaste plek
# [1, 2, 3, (1, 2), (1, 3), (2, 3)]
# totaal: 1 + 3 + 3
# test_list = [0, 1, 2, 3, 4, 5] 0 en 5 vaste plek
# [1, 2, 3, 4, (1, 2), (1, 3), (1, 4), (2, 3), (2, 4), (3, 4), (1, 2, 4), (1, 3, 4)]
# totaal: 1 + 4 + 6 + 2
# test [0, 1, 2, 3, 4, 5, 6] 0 en 6 vaste plek
# [1, 2, 3, 4, 5, (1, 2), (1, 3), (1, 4), (1, 5), (2, 3), (2, 4), (2, 5), (3, 4), (3, 5), (4, 5),
# (1, 2, 4), (1, 2, 5), (1, 3, 4), (1, 3, 5), (1, 4, 5), (2, 3, 5), (2, 4, 5), (1, 2, 4, 5)
# totaal: 1 + 5 + 10 + 7 + 1

# test_list = [0, 1, 2, 5, 6, 7] 0 en 7 vaste plek
# [1, 6, (1, 6)]
