def p1():
    with open('../stream/input06.txt', 'r') as f:
        count = sum([len(set(g) - set('\n')) for g in f.read().split("\n\n")])
    return count

def p2():
    with open('../stream/input06.txt', 'r') as f:
        count = 0
        for group in f.read().split('\n\n'):
            sharedanswers = set('abcdefghijklmnopqrstuvwxyz')
            for answer in group.splitlines():
                sharedanswers = sharedanswers.intersection(answer)
            count += len(sharedanswers)
    return count
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            