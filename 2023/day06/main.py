times = [38, 67, 76, 73]
distances = [234, 1027, 1157, 1236]
possible_options_multiplied = 1

for i, time in enumerate(times):
    possible_options = 0
    for j in range(1, time):
        if j * (time - j) > distances[i]:
            possible_options += 1

    possible_options_multiplied *= possible_options

print("1:", possible_options_multiplied)

time2 = int("".join(str(time) for time in times))
distance2 = int("".join(str(distance) for distance in distances))
possible_options = 0

for j in range(1, time2):
    if j * (time2 - j) > distance2:
        possible_options += 1

print("2:", possible_options)
