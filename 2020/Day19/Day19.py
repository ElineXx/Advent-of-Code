with open("input19.txt") as f:
    input_list = [x.split("\n") for x in f.read().split("\n\n")]

test_input1 = [
    '0: 1 2',
    '1: "a"',
    '2: 1 3 | 3 1',
    '3: "b"'
]

test_input2 = [
    '0: 4 1 5',
    '1: 2 3 | 3 2',
    '2: 4 4 | 5 5',
    '3: 4 5 | 5 4',
    '4: "a"',
    '5: "b"'
]


def make_rule_dict(rule_list):
    rule_dict = {}
    for row in rule_list:
        x, y = row.split(":")
        rule_dict[x] = [r.strip().split(" ") for r in y[1:].split("|")]
    return rule_dict


def solve_rule_0(rule_dict, key='0'):
    rules = rule_dict[key]

    return rules

test_dict1 = make_rule_dict(test_input1)
print("returned:", solve_rule_0(test_dict1))

print(input_list)
rule_dict1 = make_rule_dict(input_list[0])
print(rule_dict1)