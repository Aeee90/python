import itertools


class Solve():
    primes = [2,3,5,7,11,13,17]
    permu = itertools.permutations((i for i in range(10)))

    def convertoInt(self, tu):
        temp = ""
        for i in tu:
            temp += str(i)
        return int(temp)

    def solve(self):
        result = 0
        for i in self.permu:
            chk = True
            for j in range(1,8):
                if self.convertoInt(i[j:j+3])%self.primes[j-1] != 0:
                    chk = False
                    break

            if chk:
                result += self.convertoInt(i)
        return result

print(Solve().solve())
