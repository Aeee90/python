def solution(num):
    for a in range(num//3):
        for b in range(a+1, (num - a)//2):
            c =  num - a - b
            if a**2 + b**2 == c**2:
                return (a*b*c)


print(solution(1000))
