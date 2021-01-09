with open("input18.txt") as f:
    input_list = f.read().splitlines()
print(input_list[0])


def calculate(operations):

    operation_list = operations.strip().split(" ")
    start_op = ""
    end_op = ""

    if operation_list and not operation_list[0].isnumeric():
        start_op = operation_list.pop(0)

    if operation_list and not operation_list[-1].isnumeric():
        end_op = operation_list.pop(-1)

    if not operation_list:
        return start_op + end_op

    while len(operation_list) > 1:
        if operation_list[1] == "+":
            operation_list[:3] = [int(operation_list[0]) + int(operation_list[2])]
        elif len(operation_list) > 1 and operation_list[1] == "*":
            operation_list[:3] = [int(operation_list[0]) * int(operation_list[2])]

    return start_op + str(operation_list[0]) + end_op


for row in input_list:
    p_count = 0
    max_p_count = 0
    order_list = [[0, 0]]
    for char_no, char in enumerate(row):
        if char == "(":
            p_count += 1
            if p_count > max_p_count:
                max_p_count = p_count
            order_list.append([p_count, char_no + 1])
        elif char == ")":
            p_count -= 1
            order_list.append([p_count, char_no + 1])
    for x in range(len(order_list) - 1):
        order_list[x].append(order_list[x + 1][1] - 1)
    order_list[-1].append(len(row))

    print(order_list)
    calc_string = ""
    for j in range(len(order_list)):
        # order_list[j][1:] = [calculate(row[order_list[j][1]:order_list[j][2]])]
        calc_string += calculate(row[order_list[j][1]:order_list[j][2]])
    print(calc_string)

    if "+" in calc_string or "*" in calc_string:
        print(min(calc_string.index("+"), calc_string.index("*")))
    else:
        print(calc_string)

