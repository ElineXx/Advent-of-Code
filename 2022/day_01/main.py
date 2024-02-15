with open('input.txt') as f:
    input_list = [x.split("\n") for x in f.read().strip().split("\n\n")]
print(input_list)

total_calories_list = [sum([int(y) for y in x]) for x in input_list]
max_calories = max(total_calories_list)
print("1:", max_calories)

total_calories_list.sort()
num_top = 3
sum_top_calories = sum(total_calories_list[-num_top:])
print("2:", sum_top_calories)
