class Solution:
    odoPrimes = [1]
    def isPrimes(self, num):
        for j in range(3, int(num ** 0.5 + 1)):
            if num % j == 0:
                return False
        return True

    def isGoldHolse(self, num):
        for i in self.odoPrimes:
            if ((num - i) // 2) ** 0.5 % 1 == 0:
                return True
        return False

    def solution(self):
        num = 3
        while True:
            if self.isPrimes(num):
                self.odoPrimes.append(num)
            else:
                if not self.isGoldHolse(num):
                    return num
            num += 2

print(Solution().solution())