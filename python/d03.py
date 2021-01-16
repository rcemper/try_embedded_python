def p1():
    lines = open('../stream/input03.txt').read().splitlines()
    period = 31 #in chars

    mat = []
    for line in lines:
        mat_row = [1 if x == '#' else 0 for x in list(line)]
        mat.append(mat_row)

    count = 0
    j_ = 0
    for i in range(0, len(mat)):
     #   print(mat[i])
        j = j_ % period
        j_ += 3
        
        if (mat[i][j] == 1):
            count += 1
    return (count)

def p2():
    lines = open('../stream/input03.txt').read().splitlines()
    period = 31 #in chars

    mat = []
    for line in lines:
        mat_row = [1 if x == '#' else 0 for x in list(line)]
        mat.append(mat_row)

    ld = [
        [1,1],
        [3,1],
        [5,1],
        [7,1],
        [1,2]
    ]

    lcount = []
    for d in ld:
        dx = d[0]
        dy = d[1]
        j_ = 0
        count = 0
        for i in range(0, len(mat), dy):
            j = j_ % period
            j_ += dx
            
            if (mat[i][j] == 1):
                count += 1
        lcount.append(count)

    ans = 1
    for r in lcount:
        ans = r*ans
    return (ans)
 
if __name__ == '__main__':
    print('Part 1 : ', p1())
    print('Part 2 : ', p2())
    exit()
