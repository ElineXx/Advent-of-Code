f = open('input.txt')
modules = [int(x) for x in f.read().splitlines()]


# 1
def calc_fuel(module_mass):
    return module_mass // 3 - 2


total_fuel1 = sum([calc_fuel(x) for x in modules])
print(total_fuel1)


# 2
def calc_fuel2(module_mass):
    mass = module_mass
    fuel_sum = 0

    while True:
        mass = calc_fuel(mass)
        if mass < 0:
            break
        fuel_sum += mass

    return fuel_sum


total_fuel2 = sum([calc_fuel2(x) for x in modules])
print(total_fuel2)
