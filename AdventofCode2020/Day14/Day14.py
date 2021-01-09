f = open('input14.txt')
input_list = f.read().splitlines()

# 1
mem_dict = {}
mask = None

for row in input_list:
    if row.startswith('mask'):
        mask = row[-36:]

    if row.startswith('mem'):
        binary_str = bin(int(row.split(' = ')[1]))[2:]
        binary_str = '0' * (len(mask) - len(binary_str)) + binary_str
        new_binary_str = ''
        for i in range(len(mask)):
            if mask[i] == 'X':
                new_binary_str += binary_str[i]
            else:
                new_binary_str += mask[i]
        mem_dict[row.split(' = ')[0]] = int(new_binary_str, 2)

print(sum(mem_dict.values()))

# 2
mem_dict = {}
mask = None

for row in input_list:

    if row.startswith('mask'):
        mask = row[-36:]

    if row.startswith('mem'):
        mem_address = bin(int(''.join([x for x in row.split(' = ')[0] if x.isdigit()])))[2:]
        mem_address = '0' * (len(mask) - len(mem_address)) + mem_address
        actual_addresses = []
        first_address = ''

        for i in range(len(mask)):
            if mask[i] == '1':
                first_address += '1'
            elif mask[i] == 'X':
                first_address += '0'
            else:
                first_address += mem_address[i]

        actual_addresses.append(first_address)
        for j in range(len(mask)):
            if mask[j] == 'X':
                new_addresses = []
                for address in actual_addresses:
                    address_option = address[:j] + '1' + address[j + 1:]
                    new_addresses.append(address_option)
                actual_addresses.extend(new_addresses)
        for address in actual_addresses:
            mem_dict[int(address, 2)] = int(row.split(' = ')[1])

print(sum(mem_dict.values()))
