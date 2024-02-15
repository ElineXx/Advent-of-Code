

with open('input.txt') as f:
    calibration_strings = [x for x in f.read().strip().split("\n")]

calibration_values = []

for calibration_string in calibration_strings:
    first_digit = ""
    last_digit = ""

    for element in calibration_string:
        if element.isnumeric():
            if len(first_digit) == 0:
                first_digit = element
            last_digit = element

    calibration_values.append(int(first_digit + last_digit))

print("1:", sum(calibration_values))


calibration_values = []
digit_strings = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

for calibration_string in calibration_strings:
    first_digit = ""
    last_digit = ""

    for i, element in enumerate(calibration_string):
        if element.isnumeric():
            if len(first_digit) == 0:
                first_digit = element
            last_digit = element
        else:
            for j, digit_string in enumerate(digit_strings, 1):
                if calibration_string[i:].startswith(digit_string):
                    if len(first_digit) == 0:
                        first_digit = str(j)
                    last_digit = str(j)

    if len(first_digit) != 0:
        calibration_values.append(int(first_digit + last_digit))

print("2:", sum(calibration_values))




