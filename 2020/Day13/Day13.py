f = open('input13.txt')
input_list = f.read().splitlines()

# 1
timestamp = int(input_list[0])
bus_IDs = [int(x) for x in input_list[1].split(',') if x.isnumeric()]

first_bus = None
first_time = min(bus_IDs)
for num in bus_IDs:
    if num - (timestamp % num) < first_time:
        first_bus = num
        first_time = num - (timestamp % num)

print(first_bus * first_time)

# 2
bus_IDs2 = [(int(x), index) for index, x in enumerate(input_list[1].split(',')) if x.isnumeric()]
test = [(17, 0), (13, 2), (19, 3)]
test2 = [(1789, 0), (37, 1), (47, 2), (1889, 3)]


def find_solution(tuples):

    y = tuples
    x = 0
    step = y[0][0]
    for i in range(1, len(y)):
        while True:
            x += step
            if (x + y[i][1]) % y[i][0] == 0:
                step *= y[i][0]
                break
    return x


print(find_solution(test))
print(find_solution(test2))
print(find_solution(bus_IDs2))

