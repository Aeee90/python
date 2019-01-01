class Symmetric:
    def checkSymmetric(self, num):
        if num == num[::-1]:
            return True

        return False

    def convertBin(self, num):
        bi = ""
        aa = num
        while num//2 != 0:
            bi = str(num%2) + bi
            num //= 2
        if num == 1:
            bi = str(num) + bi
        return bi

    def searchSymmetric(self, num):
        return [i for i in range(1, num+1,2) if self.checkSymmetric(str(i)) and self.checkSymmetric(self.convertBin(i))]


print(Symmetric().searchSymmetric(1000000))
print(sum(Symmetric().searchSymmetric(1000000)))




