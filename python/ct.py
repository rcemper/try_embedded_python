import sys
import d01,d02,d03,d04,d05,d06,d07,d08,d09,d10,d11,d12
import d13,d14,d15,d16,d17,d18,d19,d20,d21,d22,d23,d24,d25
# simulate call from IRIS    

def run(mod):
    d='d'+str(mod+100)[1:]
    res1=getattr(getattr(sys.modules[__name__],d),'p1')()
    res2=getattr(getattr(sys.modules[__name__],d),'p2')()
    return res1,res2

if __name__ == '__main__':
    inp = ""
    day = 0
    print('welcome to demo test')
    print('select a day (1..25) or exit with "*"')
    while inp != '*' :
        inp = input('\twhich day : ')
        if (inp == "*") : break
        if (inp == "" ) : inp=str(day+1)   
        try:
            day = int(inp)
        except:
             print('\t\twhat was that ?',inp,' ??')
             continue
        if ((day < 1) | (day > 25)): 
            print('\t\tonly 1 .. 25 !',inp)
            continue
        res=run(day)
        print('Day ',day,' Part 1:',res[0])
        print('Day ',day,' Part 2:',res[1])
    exit()
