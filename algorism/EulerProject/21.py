class aa:
    def getDivisores(self, num):
        divisores = [1]

        for i in range(2, int(num**0.5) + 1):
            if num%i == 0:
                divisores.append(i)
                divisores.append(num//i)

        return sum(divisores)

    def solve(self, limit):
        answer = 0
        tempSave = {}
        for num in range(2, limit + 1):
            temp1 = self.getDivisores(num)
            tempSave[num] = temp1
            temp2 = tempSave.get(temp1)

            if temp1 == 1 or temp2 == 1:
                continue

            if temp2 == None:
                tempSave[temp1] = self.getDivisores(temp1)
                temp2 = tempSave.get(temp1)

            if num == temp2 and num != temp1:
                answer += temp2 + temp1

        return answer//2

print(aa().solve(10000))