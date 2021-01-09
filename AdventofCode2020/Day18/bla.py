


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
    last_string = ""
    for j in range(len(order_list)):
        # order_list[j][1:] = [calculate(row[order_list[j][1]:order_list[j][2]])]
        last_string += calculate(row[order_list[j][1]:order_list[j][2]])
    print(last_string)
