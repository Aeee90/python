
def solution(i, base):
    base_2, base_1 = base**2, base**1
    for j in range(i ,1000, i):
        if (j//base_2 + j%base_2//base_1 + j%base_2%base_1)% i is not 0:
            return None

    return i

base = 30
result = []
for i in range(2,base + 1):
    temp = solution(i, base)
    if temp is not None:
        result.append(temp)

print(result)