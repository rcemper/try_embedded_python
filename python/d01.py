
def find_multiple_twos(n, target):
    d = {}
    nums = list(map(int, n))

    for i in range(len(nums)):
        result = target - nums[i]
        if result in d:
            return nums[i] * nums[d[result]]
        else:
            d[nums[i]] = i
    return -1


def find_multiple_threes(n, target):
    nums = list(map(int, sorted(n)))
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while (l < r):
            if nums[i] + nums[l] + nums[r] == target:
                return nums[i] * nums[l] * nums[r]
            elif nums[i] + nums[l] + nums[r] < target:
                l += 1
            else:
                r -= 1
    return -1

with open('../stream/input01.txt', mode='r') as inp:
    n = [int(line.rstrip()) for line in inp] 
    p01= find_multiple_twos(n, 2020)
    p02= find_multiple_threes(n, 2020)

def p1():
    return (p01)

def p2():
    return (p02)

if __name__ == '__main__':
    print('Part 1 : ', p1())
    print('Part 2 : ', p2())
    exit()