def p1():
    with open('../stream/input17.txt', 'r') as f:
        grid = set((x, y, 0) for y, line in enumerate(f.readlines()) for x, value in enumerate(line) if value == '#')
        tmpgrid = set()
        init_height = sorted(grid, key=lambda s: s[1])[-1][1] + 1
        init_width = sorted(grid, key=lambda s: s[0])[-1][0] + 1

        for cycle in range(1, 7):
            for z in range(-cycle, cycle + 1):
                for y in range(-cycle, init_height + cycle + 1):
                    for x in range(-cycle, init_width + cycle + 1):
                        count = sum(1 for i in range(x-1, x+2) for j in range(y-1, y+2) for k in range(z-1, z+2) if (i, j, k) in grid)
                        if (x, y, z) in grid and 3 <= count <= 4:  # The cell (x,y,z) is also counted
                            tmpgrid.add((x, y, z))
                        if (x, y, z) not in grid and count == 3:
                            tmpgrid.add((x, y, z))

            grid = tmpgrid
            tmpgrid = set()
    return len(grid)

def p2():
    with open('../stream/input17.txt', 'r') as f:
        grid = set((x, y, 0, 0) for y, line in enumerate(f.readlines()) for x, value in enumerate(line) if value == '#')
        tmpgrid = set()
        init_height = sorted(grid, key=lambda s: s[1])[-1][1] + 1
        init_width = sorted(grid, key=lambda s: s[0])[-1][0] + 1

        for cycle in range(1, 7):
            for w in range(-cycle, cycle + 1):
                for z in range(-cycle, cycle + 1):
                    for y in range(-cycle, init_height + cycle + 1):
                        for x in range(-cycle, init_width + cycle + 1):
                            count = sum(1 for i in range(x-1, x+2) for j in range(y-1, y+2)
                                        for k in range(z-1, z+2) for l in range(w-1, w+2) if (i, j, k, l) in grid)
                            if (x, y, z, w) in grid and 3 <= count <= 4:  # The cell (x,y,z,w) is also counted
                                tmpgrid.add((x, y, z, w))
                            if (x, y, z, w) not in grid and count == 3:
                                tmpgrid.add((x, y, z, w))
            grid = tmpgrid
            tmpgrid = set()
      
    return len(grid)
 
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            