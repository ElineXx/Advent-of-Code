f = open('input5.txt')
input_list = f.read().split('\n')[:-1]

# 1
seat_IDs = []
for coded_ID in input_list:
    x = int(coded_ID[:-3].replace('F', '0').replace('B', '1'), 2)
    y = int(coded_ID[-3:].replace('L', '0').replace('R', '1'), 2)
    seat_IDs.append(x * 8 + y)

print(max(seat_IDs))

# 2
seat_IDs = sorted(seat_IDs)
for i in range(len(seat_IDs) - 1):
    if seat_IDs[i] != seat_IDs[i + 1] - 1:
        print(seat_IDs[i] + 1)
