def p1():
    with open('../stream/input12.txt', 'r') as f:
        data = [(line[0], int(line[1:])) for line in f]
        x = 0
        y = 0
        dx = 1  # +x => East
        dy = 0  # +y => North
        for move in data:
            if move[0] == 'N':
                y += move[1]
            elif move[0] == 'S':
                y -= move[1]
            elif move[0] == 'E':
                x += move[1]
            elif move[0] == 'W':
                x -= move[1]
            elif move[0] == 'L':
                for i in range(move[1]//90):
                    dx, dy = -dy, dx
            elif move[0] == 'R':
                for i in range(move[1]//90):
                    dx, dy = dy, -dx
            elif move[0] == 'F':
                x += move[1] * dx
                y += move[1] * dy
 #   print(f'Part 1: {abs(x) + abs(y)}')
    res1 = es2 = abs(x) + abs(y)
    return str(res1)

def p2():
    with open('../stream/input12.txt', 'r') as f:
        data = [(line[0], int(line[1:])) for line in f]
        x = 0
        y = 0
        dx = 10  # waypoint x
        dy = 1   # waypoint y
        for move in data:
            if move[0] == 'N':
                dy += move[1]
            elif move[0] == 'S':
                dy -= move[1]
            elif move[0] == 'E':
                dx += move[1]
            elif move[0] == 'W':
                dx -= move[1]
            elif move[0] == 'L':
                for i in range(move[1]//90):
                    dx, dy = -dy, dx
            elif move[0] == 'R':
                for i in range(move[1]//90):
                    dx, dy = dy, -dx
            elif move[0] == 'F':
                x += move[1] * dx
                y += move[1] * dy
 #   print(f'Part 2: {abs(x) + abs(y)}')
    res2 = abs(x) + abs(y)
    return str(res2)
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            
