import itertools

class Solution:
    def getPrimes(self, num):
        for j in range(3, int(num**0.5 + 1)):
            if num%j == 0:
                return None
        return num

    def covnerTupleToInteger(self, tu):
        temp = ""
        for i in tu:
            temp += str(i)
        return int(temp)

    def solution(self):
        for i in range(10, 0, -1):
            arr = list(itertools.permutations(list(range(1,i))))
            arr.sort(reverse=True)
            for j in arr:
                prime = self.getPrimes(self.covnerTupleToInteger(j))
                if prime != None:
                    return prime

print(Solution().solution())