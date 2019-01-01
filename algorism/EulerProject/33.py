from comm import EuclideanAlgorithm as eu

def solve():
    denominator, numerator = 1,1
    for i in range(11, 99):
        for j in range(i+1, 100):
            a10, a1, b10, b1 = i//10, i%10, j//10, j%10

            if a1 == 0 or b1 == 0 or len(set([a10, a1, b10, b1])) > 3:
                continue

            if (a10*a1)/(b10*b1) == i/j:
                denominator *= j
                numerator *= i
    return denominator//eu.getGCM(denominator, numerator)

print(solve())