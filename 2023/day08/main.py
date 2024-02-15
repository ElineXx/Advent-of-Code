import math


def calc_steps_to_end(element):
    count = 0
    while not element.endswith("Z"):
        if instructions[count % len(instructions)] == "L":
            element = node_dict[element].split(", ")[0]
        else:
            element = node_dict[element].split(", ")[1]
        count += 1

    return count


with open('input.txt') as f:
    lines = [x for x in f.read().strip().split("\n")]
instructions = lines[0]
node_dict = {key: value for key, value in [x.replace("(", "").replace(")", "").split(" = ") for x in lines][2:]}

start_elements = []
for key in node_dict.keys():
    if key.endswith("A"):
        start_elements.append(key)

steps_to_end = []
for start_element in start_elements:
    steps_to_end.append(calc_steps_to_end(start_element))

print("1:", calc_steps_to_end("AAA"))
print("2:", math.lcm(*steps_to_end))


