
class Grid:

    def see_neighbour(self, x, y, dx, dy):
        """
        Look from position (x,y) in the direction defined by (dx,dy).
        Return the position of the first chair we see in this direction.
        Return None if no chairs are visible in this direction.
        Return None if there is no chair in the current position (x,y).
        """
        if self.grid[y][x] == '.' or (dx == 0 and dy == 0):   # Makes looping easier
            return None
        x += dx
        y += dy
        while 0 <= x < self.width and 0 <= y < self.height:
            if self.grid[y][x] != '.':
                return (x, y)
            x += dx
            y += dy
        return None

    def trace_neighbours(self, x, y):
        """
        Does raytracing to find the seats seen by (x,y). Empty places are ignored.
        """
        return list(filter(lambda n: n != None, (self.see_neighbour(x, y, i, j) for i in [-1, 0, 1] for j in [-1, 0, 1])))

    def __init__(self, input, prefetch=False):
        self.grid = [[*(line.strip())] for line in input]
        self.width = len(self.grid[0])  # Assume rectangle
        self.height = len(self.grid)
        if prefetch:
            self.neighbours = {}
            for y in range(self.height):
                for x in range(self.width):
                    self.neighbours[(x, y)] = self.trace_neighbours(x, y)

    def is_occupied(self, p):
        """
        Expects a tuple p = (x,y).
        Returns True if this place is occupied, False if it is empty or outside the grid.
        """
        return 0 <= p[0] < self.width and 0 <= p[1] < self.height and self.grid[p[1]][p[0]] == '#'

    def is_available(self, x, y):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if self.is_occupied((x+i, y+j)):
                    return False
        return True

    def is_available2(self, x, y):
        for i in [-1, 0, 1]:
            for j in [-1, 0, 1]:
                if self.see_occupant(x, y, i, j):
                    return False
        return True

    def is_available2_trace(self, x, y):
        for p in self.neighbours[(x, y)]:
            if self.is_occupied(p):
                return False
        return True

    def update2_trace(self):
        """
        Update the grid using the rules in part 2.
        This time using the cached neigbours.
        """
        tmp = [row.copy() for row in self.grid]
        changed = False
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '#' and sum(self.is_occupied(p) for p in self.neighbours[(x, y)]) >= 5:
                    tmp[y][x] = 'L'
                    changed = True
                elif self.grid[y][x] == 'L' and self.is_available2_trace(x, y):
                    tmp[y][x] = '#'
                    changed = True
        self.grid = tmp
        return changed

    def see_occupant(self, x, y, dx, dy):
        """
        Look from position (x,y) in the direction defined by (dx,dy).
        Return True if the first chair in sight is occupied.
        Return False if the first chair is empty, or no chairs are visible in this direction.
        """
        if dx == 0 and dy == 0:   # Makes looping easier
            return False
        x += dx
        y += dy
        while 0 <= x < self.width and 0 <= y < self.height:
            if self.grid[y][x] == '#':
                return True
            if self.grid[y][x] == 'L':
                return False
            x += dx
            y += dy
        return False

    def update2(self):
        """
        Update the grid using the rules in part 2.
        """
        tmp = [row.copy() for row in self.grid]
        changed = False
        for y in range(self.height):
            for x in range(self.width):
                count = sum(self.see_occupant(x, y, i, j) for i in [-1, 0, 1] for j in [-1, 0, 1])
                if self.grid[y][x] == '#' and count >= 5:
                    tmp[y][x] = 'L'
                    changed = True
                elif self.grid[y][x] == 'L' and count == 0:
                    tmp[y][x] = '#'
                    changed = True
                else:
                    tmp[y][x] = self.grid[y][x]
        self.grid = tmp
        return changed

    def update1(self):
        """
        Update the grid using the rules in part 1.
        """
        tmp = [row.copy() for row in self.grid]
        changed = False
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x] == '#' and 5 <= sum(
                        self.is_occupied((x + i, y + j)) for i in [-1, 0, 1] for j in [-1, 0, 1]):
                    # >= 5, because we also count (x,y)
                    tmp[y][x] = 'L'
                    changed = True
                elif self.grid[y][x] == 'L' and self.is_available(x, y):
                    tmp[y][x] = '#'
                    changed = True
                else:
                    tmp[y][x] = self.grid[y][x]
        self.grid = tmp
        return changed

    def count_occupants(self):
        return sum(row.count('#') for row in self.grid)

    def show(self):
        print('\n'.join(''.join(row) for row in self.grid))
        print('')


def showgrid(grid):
    for y in range(len(grid)):
        print(''.join(grid[y]))
    print('')


def update(grid):
    tmp = [row.copy() for row in grid]
    changed = False
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 'L':
                seatAvailable = True
                for i in range(max(0, y-1), min(y+2, len(grid))):
                    for j in range(max(0, x - 1), min(x + 2, len(grid[y]))):
                        if grid[i][j] == '#':
                            seatAvailable = False
                            break
                    if not seatAvailable:
                        break
                if seatAvailable:
                    changed = True
                    tmp[y][x] = '#'
            elif grid[y][x] == '#':
                count = 0
                for i in range(max(0, y-1), min(y+2, len(grid))):
                    for j in range(max(0, x - 1), min(x + 2, len(grid[y]))):
                        if grid[i][j] == '#':
                            count += 1
                if count >= 5:  # 4 adjacent + the seat itself
                    changed = True
                    tmp[y][x] = 'L'
    return changed, tmp

# Part 1, class
def p1():
    with open('../stream/input11.txt', 'r') as f:
        grid = Grid(f.readlines())
        while grid.update1():
            pass
        res1 = grid.count_occupants()
    return str(res1)
 
# Part 2, caching
def p2():
    with open('../stream/input11.txt', 'r') as f:
        grid = Grid(f.readlines(), True)
        while grid.update2_trace():
            pass
        res2 = grid.count_occupants()
    return str(res2)
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            
