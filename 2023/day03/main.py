with open('input.txt') as f:
    lines = [x for x in f.read().strip().split("\n")]

sum_part_numbers = 0
sum_gear_ratios = 0

for i, line in enumerate(lines):
    number_string = ""
    for j, char in enumerate(line):
        if char.isdigit():
            number_string += char
            if j == len(line) - 1 or not line[j + 1].isdigit():
                is_part_number = False
                for k in range(i - 1, i + 2):
                    if 0 <= k <= len(lines) - 1:
                        for m in range(j - len(number_string), j + 2):
                            if 0 <= m <= len(line) - 1:
                                if lines[k][m] != "." and not lines[k][m].isdigit():
                                    is_part_number = True
                if is_part_number:
                    sum_part_numbers += int(number_string)
                number_string = ""

        if char == "*":
            numbers = []
            for y in range(i - 1, i + 2):
                if 0 <= y <= len(lines) - 1:
                    is_adjacent = False
                    number_string2 = ""
                    for x in range(j - 3, j + 4):
                        if 0 <= x <= len(line) - 1:
                            if lines[y][x].isdigit():
                                number_string2 += lines[y][x]
                                if x in range(j - 1, j + 2):
                                    is_adjacent = True
                                if x == j + 3 or not lines[y][x + 1].isdigit():
                                    if is_adjacent:
                                        numbers.append(int(number_string2))
                                        is_adjacent = False
                                    number_string2 = ""
            power = 1
            if len(numbers) > 1:
                for number in numbers:
                    power *= number
                sum_gear_ratios += power

print("1:", sum_part_numbers)
print("2:", sum_gear_ratios)