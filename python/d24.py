from re import findall
once = 0
NW = (0, 1, -1)
NE = (1, 0, -1)
W = (-1, 1, 0)
E = (1, -1, 0)
SW = (-1, 0, 1)
SE = (0, -1, 1)

DIRS = {'w': W, 'e': E, 'nw': NW, 'ne': NE, 'se': SE, 'sw': SW}


def parse_tile(tile, dirs):
    parsed = findall(r'(e|se|sw|w|nw|ne)', tile)
    moves = [dirs[mv] for mv in parsed]
    return moves


def flip_tile(tile, dirs):
    moves = parse_tile(tile, dirs)
    x, y, z = 0, 0, 0

    for move in moves:
        x += move[0]
        y += move[1]
        z += move[2]
    return x, y, z


def setup_tiles(tiles):
    black = set()

    for tile in tiles:
        flipped = flip_tile(tile, DIRS)
        if flipped not in black:
            black.add(flipped)
        else:
            black.remove(flipped)
    return black


def get_adjacent(x, y, z):
    return {(x + move[0], y + move[1], z + move[2]) for move in DIRS.values()}


def conway_hex(tiles, days, printout=False):
    black = setup_tiles(tiles)

    for day in range(1, days+1):
        to_black = set()
        to_white = set()
        to_check = set()

        for tile in black:
            to_check.add(tile)
            to_check |= get_adjacent(*tile)

        for tile in to_check:
            adjacents = get_adjacent(*tile)
            adj_black = len(adjacents & black)

            if tile in black:
                if adj_black not in (1, 2):
                    to_white.add(tile)
            else:
                if adj_black == 2:
                    to_black.add(tile)

        for tile in to_black:
            black.add(tile)
        for tile in to_white:
            black.remove(tile)
            
    return black

def p1():
    with open('../stream/input24.txt', mode='r') as inp:
        tiles = [l.rstrip() for l in inp.readlines()]   
    return str(len(setup_tiles(tiles)))

def p2():
    with open('../stream/input24.txt', mode='r') as inp:
        tiles = [l.rstrip() for l in inp.readlines()]   
    return str(len(conway_hex(tiles, 100, False)))
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            