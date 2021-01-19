import time,os,re
from collections import defaultdict

def profiler(method):
    def wrapper_method(*arg, **kw):
        t = time.time()
        ret = method(*arg, **kw)
        return ret
    return wrapper_method

@profiler
def p1():

    cnt = defaultdict(int)
    map = {}

    for l in open('../stream/input21.txt'):
        l = l.strip()

        ing = re.findall(r'(.+)\(' , l)[0].split()
        alle = re.findall(r'\(contains (.+)\)' , l)[0].replace(',' , '').split()

        for i in ing:
            cnt[i] += 1
        
        for i in alle:
            if i in map :
                map[i] &= set(ing)
            else :
                map[i] = set(ing)

    sus = set()
    for i in map.values():
        sus |= i

    answer = 0
    for i in cnt:
        if i not in sus:
            answer += cnt[i]
    return str(answer)

@profiler
def p2():

    cnt = defaultdict(int)
    map = {}

    for l in open('../stream/input21.txt'):
        l = l.strip()

        ing = re.findall(r'(.+)\(' , l)[0].split()
        alle = re.findall(r'\(contains (.+)\)' , l)[0].replace(',' , '').split()

        for i in ing:
            cnt[i] += 1

        for i in alle:
            if i in map :
                map[i] &= set(ing)
            else :
                map[i] = set(ing)

    sus = set()
    for i in map.values():
        sus |= i

    visited = defaultdict(bool)

    for _ in range(len(map)):
        for idx in map:
            if len(map[idx]) == 1 and not visited[idx]:
                visited[idx] = True
                target_idx = idx
                target_field = [e for e in map[idx]][0]
                break

        for idx in map:
            if idx == target_idx : continue
            if target_field in map[idx] : map[idx].remove(target_field)

    answer = ''
    for i in sorted(list(map.keys())):
        answer += (map[i].pop() + ',')
    
    return str(answer[:-1])

if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            