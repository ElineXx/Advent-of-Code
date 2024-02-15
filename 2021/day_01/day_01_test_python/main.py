f = open('input.txt')
modules = [int(x) for x in f.read().splitlines(-1)]

counter = 0
counter2 = 0

for i, module in enumerate(modules):
    if i > 0 and modules[i] > modules[i - 1]:
        counter += 1;
    if i > 0 and modules[i] < modules[i - 1]:
        counter2 += 1;

print(counter)
print(counter2)
