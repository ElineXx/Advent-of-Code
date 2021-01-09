import re

f = open('input16.txt')
input_list = [x.split('\n') for x in f.read().split('\n\n')]

rules = [re.findall('[0-9]+', x) for x in input_list[0]]
rules = [list(map(int, x)) for x in rules]
tickets = [re.findall('[0-9]+', x) for x in input_list[2]][1:]
tickets = [list(map(int, x)) for x in tickets]

new_tickets = []
error_rate = 0
for ticket in tickets:
    ticket_is_valid = True
    for num in ticket:
        num_is_valid = False
        for rule in rules:
            if (rule[0] <= num <= rule[1] or
                    rule[2] <= num <= rule[3]):
                num_is_valid = True
        if not num_is_valid:
            error_rate += num
            ticket_is_valid = False
    if ticket_is_valid:
        new_tickets.append(ticket)

print('1:', error_rate)

not_matches = [[0 for x in range(len(rules))] for x in range(len(rules))]
for ticket in new_tickets:
    for field, num in enumerate(ticket):
        for rule_no, rule in enumerate(rules):
            if not (rule[0] <= num <= rule[1] or
                    rule[2] <= num <= rule[3]):
                not_matches[field][rule_no] += 1

not_matches = list(zip([x for x in not_matches], [i for i in range(len(not_matches))]))
not_matches.sort(reverse=True)
keys = [x.split(': ')[0] for x in input_list[0]]

key_dict = {}
for not_match in not_matches:
    for iy, y in enumerate(not_match[0]):
        if y == 0:
            for k in range(len(not_matches)):
                not_matches[k][0][iy] = keys[iy]
            key_dict[not_match[1]] = keys[iy]

correct_keys = []
for i in range(len(key_dict)):
    correct_keys.append(key_dict[i])
my_nums = [int(x) for x in input_list[1][1].split(',')]
my_ticket = dict(zip(correct_keys, my_nums))

ans2 = 1
for field in my_ticket:
    if field.startswith('departure'):
        ans2 *= my_ticket[field]

print('2:', ans2)
