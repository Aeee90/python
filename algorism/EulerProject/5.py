#모든 수를 소인수분해해서 소인수의 최대 차수들을 구하는 방식
from comm import Prime as pr
num = 20
prime = pr.getPrimeList(num)
prime = dict(zip(prime, [0]*len(prime)))
for i in range(1, num+1):
    for key, val in prime.items():
        count = 0
        while(i%key == 0):
            count += 1
            i //= key
        prime[key] = max(prime[key], count)

result = 1
for k, v in prime.items():
    result *= k**v

print(result)

#최소공배수 버전
from comm import EuclideanAlgorithm as ec

lcm = 1
for i in range(2, 21):
    lcm = ec.getLCM(lcm, i)

print(lcm)