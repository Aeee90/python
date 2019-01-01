import copy

class CorporationSalary:

    def convBiArr(self, arr):
        biArr = [0 for i in range(len(arr))]
        l = len(arr) - 1
        for i in range(l + 1):
            print(arr[i])
            for j in range(l + 1):
                if arr[i][j] == "Y":
                  biArr[i] += 1

        return biArr


    def index(self, arr, se):
        indexArr = []
        for i in se:
            for j in range(len(arr)):
                if arr[j] == i:
                    indexArr.append(j)

        print(indexArr)
        return indexArr

    def totalSalary(self, arr):
        result = [0 for i in range(len(arr))]
        initN = "N"*len(arr)

        indexArr = self.convBiArr(arr)
        for i in self.index(indexArr, sorted(set(indexArr))):
            temp = arr[i]
            if temp == initN:
                result[i] = 1
            for j in range(len(temp)):
                if temp[j] == "Y":
                    result[i] += result[j]
        return sum(result)

print(CorporationSalary().totalSalary(["NNNNNN", "YNYNNY", "YNNNNY", "NNNNNN", "YNYNNN", "YNNYNN"]))


