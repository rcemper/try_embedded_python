def p1():
    decks = [[int(n) for n in i.splitlines()[1:]] for i in open('../stream/input22.txt').read().split('\n\n')]

    while all(decks):
        c1, c2 = decks[0].pop(0), decks[1].pop(0)
        if c1 > c2: decks[0] += [c1, c2]
        else:       decks[1] += [c2, c1]

    if decks[0]: res1 = sum(i * decks[0][-i] for i in range(1, 51))
    else:        res1 = sum(i * decks[1][-i] for i in range(1, 51))
    return str(res1)

def p2():
    decks = [[int(n) for n in i.splitlines()[1:]] for i in open('../stream/input22.txt').read().split('\n\n')]
    copy_decks = lambda decks: [[i for i in deck] for deck in decks]
    
    def game(decks):
        previous = list()
        while all(decks):
            if decks in previous: return decks
            else: previous.append(copy_decks(decks))
            c1, c2 = decks[0].pop(0), decks[1].pop(0)
            if c1 <= len(decks[0]) and c2 <= len(decks[1]):
                subdecks = copy_decks(decks)
                subdecks[0], subdecks[1] = subdecks[0][:c1], subdecks[1][:c2]
                if game(subdecks)[0]: decks[0] += [c1, c2]
                else:                 decks[1] += [c2, c1]
            elif c1 > c2: decks[0] += [c1, c2]
            else:         decks[1] += [c2, c1]
        return decks

    decks = game(decks)
    if decks[0]: res2 = sum(i * decks[0][-i] for i in range(1, 51))
    else:        res2 = sum(i * decks[1][-i] for i in range(1, 51))

    return str(res2)
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()            
