def find_marker_end(signal, marker_length):
    marker_end = 0
    for i, value in enumerate(signal):
        section = signal[i: i + marker_length]
        if len(section) == len(set(section)):
            marker_end = i + marker_length
            break

    return marker_end


with open('input.txt') as f:
    elf_signal = f.read().strip()

print("1:", find_marker_end(elf_signal, 4))
print("1:", find_marker_end(elf_signal, 14))
