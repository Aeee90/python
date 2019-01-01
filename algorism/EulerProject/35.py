from itertools import permutations as pm
class Solve:
    def getPrimes(self, num):
        primes = [2]
        for i in range(3, num+1, 2):
            ch = True
            for j in range(3, int(i**0.5 + 1)):
                if i%j == 0:
                    ch = False
                    break

            if ch:
                primes.append(i)
        return primes

    def getCircularPrimes(self, num):
        primes = self.getPrimes(num)
        circularPrimes = []
        for i in primes:
            prime = str(i)
            ch = True
            for j in range(len(prime)):
                temp = int(prime[j:] + prime[0:j])
                if temp not in primes:
                    ch = False
                    break

            if ch:
                circularPrimes.append(i)

        return circularPrimes

print(len(Solve().getCircularPrimes(1000000)))