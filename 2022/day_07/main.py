with open('input.txt') as f:
    terminal_output = f.read().strip().split("\n")
current_route = []
dir_size_dict = {}

for line in terminal_output:
    if line == "$ cd /":
        current_route = ["/"]
        continue
    if line.endswith(".."):
        current_route.pop()
        continue
    if line.startswith("$ cd"):
        current_route.append((line.split()[2]))
    if line.split()[0].isnumeric():
        dir_size_dict["/".join(current_route)] = dir_size_dict.get("/".join(current_route), 0) + int(line.split()[0])
        for i in range(1, len(current_route)):
            dir_size_dict["/".join(current_route[:-i])] = dir_size_dict.get("/".join(current_route[:-i]), 0) + int(
                line.split()[0])

total_dir_size = 0

for key, value in dir_size_dict.items():
    if value <= 100000:
        total_dir_size += value

print("1:", total_dir_size)

current_space = 70000000 - dir_size_dict["/"]
needed_space = 30000000

possible_values = []
for key, value in dir_size_dict.items():
    if dir_size_dict[key] >= needed_space - current_space:
        possible_values.append(value)

print("2:", min(possible_values))
