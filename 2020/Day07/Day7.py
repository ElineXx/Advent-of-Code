f = open('input7.txt')
input_list = f.read().split('\n')[:-1]

bag_dict = {}
for bag_string in input_list:
    x, y = bag_string.split(' contain ')
    bag_dict[x] = y.strip('.').split(', ')


# 1
def shiny_gold_finder(key):
    found_bags = ''
    for bag in bag_dict[key]:
        if 'no other' in bag:
            return ''
        if 'shiny gold' in bag:
            found_bags += key + ', '
        new_key = bag[2:]
        if not new_key.endswith('s'):
            new_key = new_key + 's'
        found_bags += shiny_gold_finder(new_key)
    if found_bags != '':
        return found_bags + key + ', '
    else:
        return ''


possible_bags = set()
for bag_key in bag_dict:
    return_value = shiny_gold_finder(bag_key).strip(', ').split(', ')
    if return_value != ['']:
        for bag_type in return_value:
            possible_bags.add(bag_type)

print(len(possible_bags))


# 2
def bag_counter(key):
    counter = 0
    for bag in bag_dict[key]:
        if 'no other' in bag:
            return 0
        counter += int(bag[0])
        new_key = bag[2:]
        if not new_key.endswith('s'):
            new_key = new_key + 's'
        counter += int(bag[0]) * bag_counter(new_key)
    return counter


print(bag_counter('shiny gold bags'))

