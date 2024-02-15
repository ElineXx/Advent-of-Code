with open('input.txt') as f:
    input_list = [x.split() for x in f.read().strip().split("\n")]
print(input_list)

win = {
    "A": "Y",
    "B": "Z",
    "C": "X",
}
draw = {
    "A": "X",
    "B": "Y",
    "C": "Z",
}
loss = {
    "A": "Z",
    "B": "X",
    "C": "Y",
}
points = {
    "win": 6,
    "draw": 3,
    "loss": 0,
    "X": 1,
    "Y": 2,
    "Z": 3,
}
total_score = 0

for shapes in input_list:
    total_score += points[shapes[1]]
    if shapes[1] == win[shapes[0]]:
        total_score += points["win"]
    if shapes[1] == draw[shapes[0]]:
        total_score += points["draw"]

print("1:", total_score)


encryption = {
    "Z": "win",
    "Y": "draw",
    "X": "loss",
}
new_total_score = 0

for shapes in input_list:
    new_total_score += points[encryption[shapes[1]]]
    if encryption[shapes[1]] == "win":
        new_total_score += points[win[shapes[0]]]
    if encryption[shapes[1]] == "draw":
        new_total_score += points[draw[shapes[0]]]
    if encryption[shapes[1]] == "loss":
        new_total_score += points[loss[shapes[0]]]

print("2:", new_total_score)
