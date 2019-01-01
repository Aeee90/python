class Solve:

    def getPrimes(self):
        self.primes = [2,3,5,7]
        i, specificPrimes = 11, []
        while len(specificPrimes) < 11:
            ch = True
            for j in range(2, int(i**0.5 + 1)):
                if i % j == 0:
                    ch = False
                    break
            if ch:
                self.primes.append(i)
                if self.check(i) is not None:
                    specificPrimes.append(i)
            i+=2
        return specificPrimes

    def check(self, num):
        temp = str(num)
        length = len(temp)
        for i in range(length):
            if int(temp[i:]) not in self.primes:
                return None
            if int(temp[:length-i]) not in self.primes:
                return None
        return num

result = Solve().getPrimes()
print(result)
print(sum(result))