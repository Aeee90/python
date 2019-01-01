from itertools import permutations

def convertNum(stx, etx, li=[]):
    ss = 0
    j = 0
    for i in range(stx, etx+1):
        ss += li[i]*(10**j)
        j += 1
    return ss

numPer = list(permutations([i for i in range(10)], 10))
#numPer = [[i for i in range(10)]]
result = set([])
for li in numPer:
    for i in range(8):
        for j in range(i+1, 9):
            a, b, c = convertNum(0, i, li), convertNum(i+1, j, li), convertNum(j+1, 9, li)
            if a * b == c:
                print("{} {} {}".format(a, b, c))
                result.add(c)

print(sum(result))
