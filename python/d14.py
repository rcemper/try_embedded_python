from itertools import product

d0 = [ x.replace('[', ' = ').replace(']', '').split(' = ') for x in open('../stream/input14.txt').read().splitlines() ]

def sum(ram, b):
    c = 0
    for x in ram:
        c += int(ram[x], b)
    return c

def p1():
    d=d0
    ram = {}
    mask = []
    for instruction in d:
        cmd = instruction[0]
        if cmd == 'mask':
            mask = list(instruction[1])
        elif cmd == 'mem':
            b = list(bin(int(instruction[2]))[2:].zfill(36))
            for x in range(len(mask)):
                if mask[x] != 'X':
                    b[x] = mask[x]
            ram[int(instruction[1])] = ''.join(b)
    return str(sum(ram, 2))

def p2():
    d=d0
    ram = {}
    mask = []
    for instruction in d:
        cmd = instruction[0]
        if cmd == 'mask':
            mask = list(instruction[1])
        elif cmd == 'mem':
            b = list(bin(int(instruction[1]))[2:].zfill(36))
            for x in range(len(mask)):
                if mask[x] != '0':
                    b[x] = mask[x]
            b = ''.join(b)
            b_ft = b.replace('X', '{}') 
            for i in product('01', repeat=b.count('X')):
                addr = int(b_ft.format(*i),2)
                ram[addr] = instruction[2]
    return str(sum(ram, 10))

if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            
