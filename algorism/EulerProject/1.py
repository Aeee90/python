from comm import EuclideanAlgorithm as euc
from comm import Series as seri

def solve(n, a, b):
    n -= 1
    lcm = euc.getLCM(a, b)
    return seri.arithmeticSeries(a, n//a) + seri.arithmeticSeries(b, n//b) - seri.arithmeticSeries(lcm, n//lcm)

print(solve(1000, 3, 5))