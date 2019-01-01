results = {}
def solution(num):
    count = 0
    while(num>1):
        num = num //2 if num%2 is 0 else 3*num +1
        count += 1

        if results.get(num) is not None:
            return results[num] + count

    return count

num = 1000000
max = 1
for i in range(1, num + 1):
    results[i] = solution(i)
    if results.get(max) < results.get(i):
        max = i

print(max)