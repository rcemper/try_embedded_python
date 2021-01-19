import itertools
once = 0
res = (0,0)
rules = ""

def find(val):
    global rules
    temp = []
    if '"' in val:
        return [[val.strip('"')],[]]
    elif '|' in val:
        for pair in val.split(' | '):
            temp.append([find(rules[x]) for x in pair.split(' ')])
    else:
        temp.append([find(rules[x]) for x in val.split(' ')])
    return [[''.join(list(x)) for x in itertools.product(*[sum(z,[]) for z in y])] for y in temp]

def calc():
    global once,res,rules
    if once > 0 : return
    with open("../stream/input19.txt", 'r') as file:
        ruledata, data = [x.split('\n') for x in file.read().split('\n\n')]
        rules = {x.split(':')[0] : x.split(': ')[1] for x in ruledata}
        result, result_8, result_11 = find(rules['0']), find(rules['8'])[0], find(rules['11'])[0]
        res1 = len([x for x in data if x in result[0]])
        valids, max_8, max_11 = [], len(max(result_8)), len(max(result_11))
        for y in data:
            if len(y)%max_8 != 0:
                continue
            for x in range(max_11, len(y), max_11):
                elevens = int(x/max_11)
                eights = int((len(y) - elevens*max_11)/max_8)
                for z in range(1, eights+1):
                    if not y[int(max_8*z-max_8):int(max_8*z)] in result_8:
                        break
                else:
                    w = y[eights*max_8:]
                    for z in range(1, elevens+1):
                        if not w[:int(max_11/2)]+w[-int(max_11/2):] in result_11:
                            break
                        w = w[int(max_11/2):-int(max_11/2)]
                    else:
                         valids.append(y)
                         break
        res2=len(valids)
    res = (res1,res2)
    return
   
def p1():
    global once
    calc()
    once = 1
    return str()res[0])
def p2():
    global once
    calc()
    once = 1
    return str(res[1])
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()    
