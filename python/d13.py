import sys
from math import ceil

def p1():
    with open("../stream/input13.txt", "r") as file:
        data = [x.strip() for x in file.read().splitlines()]
        time, busses = [int(data[0]), [(int(x) if x != 'x' else x) for x in data[1].split(',')]]
        schedule = {bus:bus*int(ceil(float(time)/float(bus)))-time for bus in busses if bus != 'x'}
        indexes = {busses[i]:i for i in range(len(busses))}
        first_bus, index_first_bus = busses[0], indexes[busses[0]]
        while True:
            marker = 0
            interval_to_compare = first_bus
            for bus in sorted([bus for bus in busses if bus != 'x'], reverse=True)[:-1]:
                valids = []
                while True:
                    marker += interval_to_compare
                    offset = float(marker + indexes[bus] - index_first_bus)/float(bus)
                    if offset == int(offset):
                        valids.append(int(offset)*bus)
                    if len(valids) == 2:
                        marker = valids[0] - indexes[bus]
                        interval_to_compare = valids[1]-valids[0]
                        break
                else:
                    continue
            break 
    res1 = [k*v for k,v in schedule.items() if v == min([x for x in schedule.values()])]
    return str(res1[0])
 
def p2():
    with open("../stream/input13.txt") as infile:

        est_time = infile.readline().strip()
        buses = [(int(b), c) for c, b in enumerate(infile.readline().strip().split(',')) if b != 'x']

        increment = 1
        n0 = 0
        b0 = buses[0]
        for b in buses[1:]:
            while (b0[0] * n0 - b0[1] + b[1]) % b[0] != 0:
                n0 += increment
            increment *= b[0]
    res2 = b0[0] * n0 - b0[1]
    return str(res2)
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            
