from operator import itemgetter

with open('input.txt') as f:
    lines = [x.split() for x in f.read().strip().split("\n")]
cards = ["2", "3", "4", "5", "6", "7", "8", "9", "T", "J", "Q", "K", "A"]

for line in lines:
    count_dict = {}
    card_values = []
    for card in line[0]:
        card_values.append(cards.index(card))
        if card in count_dict:
            count_dict[card] += 1
        else:
            count_dict[card] = 1
    line.append(sorted(count_dict.values(), reverse=True)[:2])
    line.append(card_values)

lines = sorted(lines, key=lambda x: (x[2], x[3]))
total_winnings = 0
for i, line in enumerate(lines, 1):
    total_winnings += i * int(line[1])

print("1:", total_winnings)


cards2 = ["J", "2", "3", "4", "5", "6", "7", "8", "9", "T", "Q", "K", "A"]

for line in lines:
    if line[0] == "JJJJJ":
        line[2] = [5]
        line[3] = [0, 0, 0, 0, 0]
        continue

    count_dict = {}
    card_values = []
    j_count = 0
    for card in line[0]:
        card_values.append(cards2.index(card))
        if card == "J":
            j_count += 1
        else:
            if card in count_dict:
                count_dict[card] += 1
            else:
                count_dict[card] = 1
    pairs = sorted(count_dict.values(), reverse=True)[:2]
    pairs[0] += j_count
    line[2] = pairs
    line[3] = card_values

lines = sorted(lines, key=lambda x: (x[2], x[3]))
total_winnings2 = 0
for i, line in enumerate(lines, 1):
    total_winnings2 += i * int(line[1])

print("2:", total_winnings2)

