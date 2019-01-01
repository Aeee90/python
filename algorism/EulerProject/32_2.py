import copy

def getDivisores(num):
    divisores = []

    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            divisores.append(i)

    return divisores

def checkVaild(i, vaild = []):
    for i in str(i):
        if i == "0":
            return None

        if i in vaild:
            return None
        vaild.append(i)

    return vaild


def solve():
    result = []
    for c in range(965*87 + 1):
   # for c in [7254]:

        vaild = checkVaild(c, [])
        if vaild == None:
            continue

        for a in getDivisores(c):
            temp = copy.copy(vaild)
            temp = checkVaild(a, temp)
            if temp == None:
                continue

            temp = checkVaild(c//a, temp)
            if temp == None:
                continue
            if len(temp) == 9:
                result.append(c)
                break

    return result

print(sum(solve()))