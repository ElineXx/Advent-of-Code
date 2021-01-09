f = open('input12.txt')
input_list = f.read().splitlines()
split_list = [[x[0], int(x[1:])] for x in input_list]


# 1
def find_position1(actions):

    position = [0, 0]
    directions = ('E', 'S', 'W', 'N')
    r = 0

    for action in actions:
        x = action[0]
        y = action[1]

        if x == 'F':
            x = directions[r]
        if x == 'L':
            r = int((r - y / 90) % 4)
        if x == 'R':
            r = int((r + y / 90) % 4)
        if x == 'E':
            position[0] += y
        if x == 'W':
            position[0] -= y
        if x == 'S':
            position[1] += y
        if x == 'N':
            position[1] -= y

    return position


position1 = find_position1(split_list)
print(abs(position1[0]) + abs(position1[1]))


# 2
def find_position2(actions):

    pos = [0, 0]
    waypoint_pos = [10, -1]

    for action in actions:
        x = action[0]
        y = action[1]

        if x == 'F':
            pos[0] += y * waypoint_pos[0]
            pos[1] += y * waypoint_pos[1]

        if x == 'L':
            y = -y
        if x in 'LR':
            for i in range(((y // 90) % 4)):
                a = waypoint_pos[0]
                b = waypoint_pos[1]
                waypoint_pos = [-b, a]

        if x == 'E':
            waypoint_pos[0] += y
        if x == 'W':
            waypoint_pos[0] -= y
        if x == 'S':
            waypoint_pos[1] += y
        if x == 'N':
            waypoint_pos[1] -= y

    return pos


position2 = find_position2(split_list)
print(abs(position2[0]) + abs(position2[1]))
