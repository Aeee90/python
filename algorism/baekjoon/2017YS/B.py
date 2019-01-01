N = int(input())
sooup = []
for i in range(N):
    _, *temp = input().split(" ")
    sooup.append(set(temp))

M = int(input())
student = []
for i in range(M):
    _, *temp = input().split(" ")
    temp = set(temp)

    count = 0
    for a in sooup:
        if len(a - temp) is 0:
            count += 1
    print(count)