with open('input.txt') as f:
    lines = [[y.split(":")[-1].strip() for y in x.split("|")]for x in f.read().strip().split("\n")]
lines = [[y.split() for y in x] for x in lines]

total_score = 0

for line in lines:
    winning_numbers, numbers = line
    score = 0
    for number in numbers:
        if number in winning_numbers:
            if score == 0:
                score += 1
            else:
                score *= 2
    total_score += score

print("1:", total_score)


matches_dict = {}
for i, line in enumerate(lines, 1):
    winning_numbers, numbers = line
    matches = 0
    for number in numbers:
        if number in winning_numbers:
            matches += 1
    matches_dict[i] = matches


def get_cards(card):
    count = 1
    if matches_dict[card] == 0:
        return count
    for new_card in range(card + 1, card + matches_dict[card] + 1):
        if new_card in range(1, len(matches_dict) + 1):
            count += get_cards(new_card)

    return count


total_cards = 0
for key in matches_dict.keys():
    total_cards += get_cards(key)

print("2:", total_cards)
