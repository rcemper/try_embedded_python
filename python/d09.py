def main():
    with open('../stream/input09.txt', 'r') as f:
        numbers = [int(d.strip()) for d in f]
     
    for i in range(25, len(numbers)):
        if numbers[i] not in [a + b for a in numbers[i - 25:i] for b in numbers[i - 25:i] if a != b]:
            target = numbers[i]
    #          print(f'Part 1: {target}')
            break
         
    summed = numbers.copy()
    for i in range(1, len(numbers)):
        summed[i] += summed[i - 1]
    for i in range(len(numbers)):
        for j in range(i+2, len(numbers)):
            if summed[j] - summed[i] == target:
                # summed[j]-summed[i] gives the sum of numbers[i+1]..numbers[j]
    #                print(f'Part 2: {min(numbers[i+1:j]) + max(numbers[i+1:j])}')
                res2 = min(numbers[i+1:j]) + max(numbers[i+1:j])
            if summed[j] - summed[i] > target:
                break
    return (target,res2)
    
def p1():
    res=main()
    return str(res[0])
def p2(): 
    res=main()
    return str(res[1])

if __name__ == '__main__':
    print('part 1: ',p1())
    print('part 2: ',p2())
    exit()       

