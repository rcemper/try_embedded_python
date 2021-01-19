once = 0
res = (0,0)

def calc():
    global once, res
    if once > 0: return
    with open("../stream/input15.txt", "r") as file:
        data = [int(y) for y in [x.strip() for x in file.read().splitlines()][0].split(',')]
        occurences = {data[i-1]:[i] for i in range(1, len(data)+1)}
        current = data[-1]
        for i in range(len(data)+1,30000001):
            if len(occurences[current]) == 1:
                current = 0
                if len(occurences[0]) == 2:
                    occurences[0].remove(occurences[0][0])
                occurences[0].append(i)
            else:
                new = occurences[current][1] - occurences[current][0]
                if new in occurences:
                    if len(occurences[new]) == 2:
                        occurences[new].remove(occurences[new][0])
                    occurences[new].append(i)
                else:
                    occurences[new] = [i]
                current = new
            if i == 2020:
                res1 = current
        res = (res1,current)
        return
        
def p1():
    global once, res
    calc()
    once = 1
    return str(res[0])
def p2():
    global once, res
    calc()
    once = 1
    return str(res[1])
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            
