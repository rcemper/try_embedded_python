def p1():
    with open('../stream/input25.txt', 'r') as f:
            pk_card = int(f.readline())
            pk_door = int(f.readline())
            loopsize_card = 0
            num = 1
            while num != pk_card:
                num = (num * 7) % 20201227
                loopsize_card += 1
            loopsize_door = 0
            num = 1
            while num != pk_door:
                num = num * 7 % 20201227
                loopsize_door += 1
            num = 1
            for i in range(loopsize_card):
                 num = num * pk_door % 20201227
            res1=num
            num = 1
            for i in range(loopsize_door):
                num = num * pk_card % 20201227
            res2=num
    return res1
    
def p2():
    return 'thanks for following this demo'
    
if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()                