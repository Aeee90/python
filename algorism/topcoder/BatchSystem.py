class BatchSystem:
    def solve(self, duration, user):
        allocateMap = {}
        allocateSumMap = {}
        for i in range(len(user)):
            temp = [] if allocateMap.get(user[i]) == None else allocateMap.get(user[i])
            tempSum = 0 if allocateSumMap.get(user[i]) is None else allocateSumMap.get(user[i])
            temp.append(duration[i])

            allocateMap[user[i]] = temp
            allocateSumMap[user[i]] = tempSum + duration[i]

        print(user)
        print(self.sort(allocateSumMap))
        result = []
        for i in self.sort(allocateSumMap):
            n = 0
            for k in range(len(allocateMap.get(i))):
                for j in range(n,len(user)):
                    if i == user[j]:
                        result.append(j)
                        n = j + 1
                        break
        return result

    def sort(self, source = {}):
        userList = list(source.keys())
        for i in range(len(userList) - 1):
            for j in range(len(userList) - 1 - i):
                sPrev, sNext = str(userList[j]), str(userList[j+1])
                if source.get(sPrev) > source.get(sNext):
                    userList[j] , userList[j+1] = sNext, sPrev
                elif source.get(userList[j]) == source.get(userList[j+1]):
                    userList[j], userList[j + 1] = sorted([sPrev, sNext])
        return userList

print(BatchSystem().solve([400,100,100,100], ["Danny Messer", "Stella Bonasera", "Stella Bonasera", "mac Taylor"]))
print(BatchSystem().solve([200, 200, 200], ["Gil", "Warrick", "Sarah"]))
print(BatchSystem().solve([100, 200, 50], ["Horatio Caine", "horatio caine", "YEAAAAAAH"]))


