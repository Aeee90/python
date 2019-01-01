def solve():
    result = 0
    for i in range(2, (9**5)*6 + 1):
        if sum([int(j)**5 for j in str(i)]) == i:
            result += i

    return result

print(solve())