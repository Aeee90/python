def solve(colleagues):
    minVal = min(colleagues)
    case = []

    for j in range(3):
        temp = 0
        for i in colleagues:
            i = i - minVal + j
            temp += int(i//5) + int(i%5//2) + int(i%5%2//1)

        case.append(temp)


    return min(case)

T = int(input())
for i in range(T):
    N = int(input())
    colleagues = list(map(lambda x: int(x), input().split(" ")))
    print(solve(colleagues))