import re

keyval_pat = re.compile(r'([a-z]{3}):(\S+)')
colour_pat = re.compile(r'#[0-9a-fA-F]{6}')
passid_pat = re.compile(r'\d{9}')


def extract_pass(data):
    return {k: v for k, v in keyval_pat.findall(data)}


def validate_intrange(txt, min, max):
    return txt.isdigit() and int(txt) >= min and int(txt) <= max


def validate_passdata(data):
    if 'byr' not in data or not validate_intrange(data['byr'], 1920, 2002):
        return False
    if 'iyr' not in data or not validate_intrange(data['iyr'], 2010, 2020):
        return False
    if 'eyr' not in data or not validate_intrange(data['eyr'], 2020, 2030):
        return False
    if 'hgt' not in data:
        return False
    elif data['hgt'].endswith('cm'):
        if not validate_intrange(data['hgt'][:-2], 150, 193):
            return False
    elif data['hgt'].endswith('in'):
        if not validate_intrange(data['hgt'][:-2], 59, 76):
            return False
    else:   # suffix wrong (neither cm nor in)
        return False
    if 'hcl' not in data or not colour_pat.fullmatch(data['hcl']):
        return False
    if 'ecl' not in data or data['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        return False
    if 'pid' not in data or not passid_pat.fullmatch(data['pid']):
        return False
    return keyref.issuperset(data.keys())

with open('../stream/input04.txt', 'r') as f:
    passportdata = re.split(r'\n\s*\n', f.read().strip())

keyref = set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'])
# Part 1
count = 0
for entry in passportdata:
    passport = set([d.split(':')[0] for d in re.split(r'\s+', entry)])
    if passport.issubset(keyref):
        if passport.issuperset(keyref):
            count += 1
        elif passport.symmetric_difference(keyref).issubset(['cid']):
            count += 1
res1=count
# Part 2
passports = [extract_pass(entry) for entry in passportdata]
count = sum(1 for data in passports if validate_passdata(data))
res2=count

def p1():
    return str(res1)

def p2():
    return str(res2)
    

if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()