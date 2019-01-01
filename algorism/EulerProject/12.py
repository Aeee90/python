def solution(limitNum):
    i, num = 1, 0
    while(True):
        num += i

        count = 0
        for j in range(1, int(num**0.5) + 1):
            if num%j == 0:
                count += 2

            if count >= limitNum:
                return num

        i += 1

print(solution(500))