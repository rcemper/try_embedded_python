def p1():
    lines = open("../stream/input02.txt").read().splitlines()
    count = 0
    for line in lines:
        line = line.replace('-',' ').replace(':','').split(' ')
        if int(line[0]) <= line[3].count(line[2]) <= int(line[1]):
            count = count + 1
    return str(count)        

def p2():
    lines = open("../stream/input02.txt").read().splitlines()
    count = 0
    for line in lines:
        line = line.replace('-',' ').replace(':','').split(' ')
        strarr = list(line[3])
        v = 0
        if strarr[int(line[0])-1] == line[2]:
            v = v + 1
        if strarr[int(line[1])-1] == line[2]:
            v = v + 1
        if v == 1:
            count = count + 1
    return str(count)

if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()