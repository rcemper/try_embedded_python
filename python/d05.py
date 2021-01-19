table = {'F': '0', 'B': '1', 'L': '0', 'R': '1'}

with open('../stream/input05.txt', 'r') as f:
    seats = [int(''.join(table[c] for c in line.strip()), 2) for line in f]
#    print(f'Part 1: {max(seats)}')
    res1 = max(seats)
    for id in range(max(seats)):
        if id not in seats and id - 1 in seats and id + 1 in seats:
#            print(f'Part 2: {id}')
            res2=id
            break

def p1():
    return str(res1)
def p2():
    return str(res2)
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            
