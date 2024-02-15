f = open('input4.txt')
input_list = f.read().split('\n')[:-1]
passports = ' '.join(input_list).split('  ')

# 1
required_fields = {'byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:'}
valid_counter1 = 0
for passport in passports:
    if all(x in passport for x in required_fields):
        valid_counter1 += 1

print(valid_counter1)

# 2
valid_counter2 = 0
for passport in passports:
    passport_dict = {}
    for i in passport.split(' '):
        x = i.split(':')
        passport_dict[x[0]] = x[1]
    try:
        if (1920 <= int(passport_dict['byr']) <= 2002 and
                2010 <= int(passport_dict['iyr']) <= 2020 and
                2020 <= int(passport_dict['eyr']) <= 2030 and
                passport_dict['hcl'][0] == '#' and
                all(x in '0123456789abcdef' for x in passport_dict['hcl'][1:]) and
                passport_dict['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth') and
                len(passport_dict['pid']) == 9 and passport_dict['pid'].isdigit() and
                (passport_dict['hgt'].endswith('cm') and
                 150 <= int(passport_dict['hgt'][:-2]) <= 193 or
                 passport_dict['hgt'].endswith('in') and
                 59 <= int(passport_dict['hgt'][:-2]) <= 76)):
            valid_counter2 += 1
    except KeyError:
        pass
    except ValueError:
        pass

print(valid_counter2)
