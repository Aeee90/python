def isPentagonal(n):
    return ((24*n + 1)**0.5 + 1)/6%1 == 0


def isHexagonal(n):
    return ((8*n + 1)**0.5 + 1)/4%1 == 0


def getTriangular(n):
    return n * (n + 1) // 2

def solution():
    n = 285
    while(True):
        n += 1
        triNum = getTriangular(n)
        if isPentagonal(triNum):
            if isHexagonal(triNum):
                return triNum

print(solution())