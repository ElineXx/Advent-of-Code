with open("input18.txt") as f:
    input_list = [x.replace(" ", "") for x in f.read().splitlines()]


# 1
def calculate_string(string):
    start_op = ""
    end_op = ""

    if string and not string[0].isdigit():
        start_op = string[0]
        string = string[1:]
    if string and not string[-1].isdigit():
        end_op = string[-1]
        string = string[:-1]

    if string:
        while not string.isnumeric():

            for i, char1 in enumerate(string):
                if not char1.isdigit():
                    num1 = string[:i]
                    op = char1

                    if string[i + 1:].isnumeric():
                        num2 = string[i + 1:]
                    else:
                        for j, char2 in enumerate(string[i + 1:]):
                            if not char2.isdigit():
                                num2 = string[i + 1:][:j]
                                break
                    break

            if op == "+":
                x = str(int(num1) + int(num2))
            elif op == "*":
                x = str(int(num1) * int(num2))

            if string[i + 1:].isnumeric():
                string = x
            else:
                string = x + string[i + 1:][j:]

    return start_op + string + end_op


def make_order_list(line):
    p_count = 0
    order_list = [[0, 0]]

    for char_no, char in enumerate(line):
        if char == "(":
            p_count += 1
            order_list.append([p_count, char_no + 1])
        elif char == ")":
            p_count -= 1
            order_list.append([p_count, char_no + 1])

    for x in range(len(order_list) - 1):
        order_list[x].append(order_list[x + 1][1] - 1)
    order_list[-1].append(len(line))

    for k in range(len(order_list)):
        order_list[k][1:] = [line[order_list[k][1]:order_list[k][2]]]

    return order_list


sum_of_values = 0

for row in input_list:
    order = make_order_list(row)
    order_max = sorted(order, reverse=True)[0][0]

    for m in range(order_max, -1, -1):
        part_string = ""
        new_order = []
        for n in range(len(order)):
            if order[n][0] >= m:
                part_string += order[n][1]
            else:
                if part_string:
                    new_order.append([m, calculate_string(part_string)])
                part_string = ""
                new_order.append(order[n])
        if part_string:
            new_order.append([m, calculate_string(part_string)])
        order = new_order

    sum_of_values += int(order[0][1])

print("1:", sum_of_values)

# 2
sum_of_values2 = 0

for row in input_list:
    while "+" in row:
        p = row.index("+")

        counter1 = 0
        start_i = -1
        for q1 in range(p - 1, -1, -1):
            if counter1 == 0 and row[q1] in "+*(":
                start_i = q1
                break
            if row[q1] == ")":
                counter1 += 1
            if row[q1] == "(":
                counter1 -= 1

        counter2 = 0
        end_i = len(row)
        for q2 in range(p + 1, len(row)):
            if counter2 == 0 and row[q2] in "+*)":
                end_i = q2
                break
            if row[q2] == "(":
                counter2 += 1
            if row[q2] == ")":
                counter2 -= 1

        new_row = (row[:start_i + 1] + "(" + row[start_i + 1:p] + "-" +
                   row[p + 1:end_i] + ")" + row[end_i:])
        row = new_row

    row = row.replace("-", "+")
    sum_of_values2 += eval(row)

print("2:", sum_of_values2)
